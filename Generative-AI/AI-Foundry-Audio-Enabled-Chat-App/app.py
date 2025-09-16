# This code is using Azure AI Foundry Python SDK

import os
import io
import wave
import base64
import sounddevice as sd
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential

def main():
    # Load environment variables from .env file
    load_dotenv()

    endpoint = os.getenv("PROJECT_ENDPOINT", "")            
    deployment = os.getenv("MODEL_DEPLOYMENT", "")       

    # Use Azure AI Foundry Project Client. Use Microsoft Entra ID authentication
    # Use AZ Login on command line to authenticate
    project_client = AIProjectClient(
        credential=DefaultAzureCredential(),
        endpoint=endpoint,
    )



    # Get OpenAI chat client
    openai_client = project_client.get_openai_client(api_version="2024-10-21")

    # Initialize prompt with system message
    chat_prompt = [
        {
            "role": "system",
            "content": [
                {
                    "type": "text",
                    "text": "You are a travel assistant that provides information on travel services."
                }
            ]
        }
    ]         


    print("Type your prompt and press Enter, or type /voice for microphone input. Type 'quit' to exit.")
    while True:
        user_input = input("Enter prompt or /voice (quit to exit): ").strip()
        if user_input.lower() == "quit":
            break
        if user_input == "/voice":
            try:
                audio_data, audio_format = record_audio()
            except Exception as e:
                print(f"Audio recording failed: {e}")
                continue
            prompt = input("Optional: Enter text prompt to send with audio (or leave blank): ")
            user_content = []
            if prompt:
                user_content.append({"type": "text", "text": prompt})
            user_content.append({
                "type": "input_audio",
                "input_audio": {
                    "data": audio_data,
                    "format": audio_format
                }
            })
        else:
            if not user_input:
                print("Please enter a prompt or /voice (quit to exit).")
                continue
            user_content = [{"type": "text", "text": user_input}]

        messages = [
            chat_prompt[0],
            {"role": "user", "content": user_content}
        ]
        response = openai_client.chat.completions.create(
            model=deployment,
            messages=messages,
            max_tokens=800,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False
        )
        print(response.choices[0].message.content)

    openai_client.close()


def record_audio(duration=5, sample_rate=16000):
    print(f"Recording for {duration} seconds. Speak now...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    buf = io.BytesIO()
    with wave.open(buf, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio.tobytes())
    wav_bytes = buf.getvalue()
    audio_data = base64.b64encode(wav_bytes).decode('utf-8')
    return audio_data, 'wav'

if __name__ == "__main__":
    main()
    