
import os
from dotenv import load_dotenv
from datetime import datetime
from azure.core.credentials import AzureKeyCredential
import azure.cognitiveservices.speech as speech_sdk


def main():
    
    global speech_config

    # Load environment variables from .env file
    load_dotenv()

    speech_region = os.getenv("SPEECH_SERVICE_REGION", "")            
    speech_key = os.getenv("SPEECH_SERVICE_KEY", "")       
    
    # Configure speech service
    speech_config = speech_sdk.SpeechConfig(speech_key, speech_region)
    print('Ready to use speech service in:', speech_config.region)

    
    # Synthesize speech
    synthesize_speech()

    # Synthesize speech with customization
    synthesize_with_customization()

    # Synthesize speech with Mic and Speaker
    synthesize_speech_mic_speaker()



def TranscribeCommand_from_speech_file():
    command = ''

    # Configure speech recognition
    current_dir = os.getcwd()
    audioFile = current_dir + '/time.wav'
    audio_config = speech_sdk.AudioConfig(filename=audioFile)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)

    # Process speech input
    print("Listening...")
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command

def TranscribeCommand_from_mic():
    # Configure speech recognition

    # Use mic to capture capture spoken input for speech recognition
    audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
    print('Speak now...')

    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
    else:
        print(speech.reason)
        if speech.reason == speech_sdk.ResultReason.Canceled:
            cancellation = speech.cancellation_details
            print(cancellation.reason)
            print(cancellation.error_details)

    # Return the command
    return command


def synthesize_speech():

    command = TranscribeCommand_from_speech_file()
    if command.lower() != 'what time is it?':
        return

    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour,now.minute)

    # Configure speech synthesis
    output_file = "output.wav"
    speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
    audio_config = speech_sdk.audio.AudioConfig(filename=output_file)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config, audio_config,)

    # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)
    else:
        print("Spoken output saved in " + output_file)

    # Print the response
    print(response_text)

def synthesize_with_customization():

    command = TranscribeCommand_from_speech_file()
    if command.lower() != 'what time is it?':
        return

    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour,now.minute)

    # Configure speech synthesis
    output_file = "output_with_customization.wav"
    speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
    audio_config = speech_sdk.audio.AudioConfig(filename=output_file)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config, audio_config,)

    responseSsml = " \
    <speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='en-US'> \
        <voice name='en-GB-LibbyNeural'> \
            {} \
            <break strength='weak'/> \
            Time to end this lab! \
        </voice> \
    </speak>".format(response_text)

    speak = speech_synthesizer.speak_ssml_async(responseSsml).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)
    else:
        print("Spoken output saved in " + output_file)


def synthesize_speech_mic_speaker():
    now = datetime.now()
    response_text = 'The time is {}:{:02d}'.format(now.hour,now.minute)
    
    command = TranscribeCommand_from_mic()
    if command.lower() != 'what time is it?':
        return
    
    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = "en-GB-RyanNeural"
    audio_config = speech_sdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config, audio_config)

    # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)




if __name__ == "__main__":
    main()