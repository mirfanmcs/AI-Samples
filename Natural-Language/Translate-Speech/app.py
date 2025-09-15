
import os
from dotenv import load_dotenv
from datetime import datetime
from azure.core.credentials import AzureKeyCredential
import azure.cognitiveservices.speech as speech_sdk


def main():
    
    global translation_config
    global speech_config

    # Load environment variables from .env file
    load_dotenv()

    speech_region = os.getenv("SPEECH_SERVICE_REGION", "")            
    speech_key = os.getenv("SPEECH_SERVICE_KEY", "")       
    
    # Configure speech service
    translation_config = speech_sdk.translation.SpeechTranslationConfig(subscription=speech_key, region=speech_region)


    translation_config.speech_recognition_language = 'en-US'
    translation_config.add_target_language('fr')
    translation_config.add_target_language('es')
    translation_config.add_target_language('hi')
    print('Ready to translate from',translation_config.speech_recognition_language)
    
    # Configure speech
    speech_config = speech_sdk.SpeechConfig(speech_key, speech_region)
    print('Ready to use speech service in:', speech_config.region)

    translate_speech()
    translate_speech_mic_speaker()



def translate_from_speech_file(targetLanguage):

    
    current_dir = os.getcwd()
    audioFile = current_dir + '/station.wav'
    audio_config_in = speech_sdk.AudioConfig(filename=audioFile)
    translator = speech_sdk.translation.TranslationRecognizer(translation_config, audio_config = audio_config_in)
    print("Getting speech from file...")
    result = translator.recognize_once_async().get()
    print('Translating "{}"'.format(result.text))
    translation = result.translations[targetLanguage]
    print(translation)
    return translation


def translate_from_mic(targetLanguage):
  # Translate speech
    audio_config_in = speech_sdk.AudioConfig(use_default_microphone=True)
    translator = speech_sdk.translation.TranslationRecognizer(translation_config, audio_config = audio_config_in)
    print("Speak now...")
    result = translator.recognize_once_async().get()
    print('Translating "{}"'.format(result.text))
    translation = result.translations[targetLanguage]
    print(translation)
    return translation
 

def translate_speech():
 
    # Get user input
    targetLanguage = ''
    targetLanguage = input('\nEnter a target language\n fr = French\n es = Spanish\n hi = Hindi\n Enter anything else to stop\n').lower()
    if targetLanguage not in translation_config.target_languages:
        return
    
    print('Translating to', targetLanguage)

    translation = translate_from_speech_file(targetLanguage)
    if not translation:
        return  
    
    # Synthesize translation to file
    output_file = "output.wav"
    voices = {
            "fr": "fr-FR-HenriNeural",
            "es": "es-ES-ElviraNeural",
            "hi": "hi-IN-MadhurNeural"
    }
    speech_config.speech_synthesis_voice_name = voices.get(targetLanguage)
    audio_config_out = speech_sdk.audio.AudioConfig(filename=output_file)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config, audio_config_out)
    speak = speech_synthesizer.speak_text_async(translation).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)
    else:
        print("Spoken output saved in " + output_file)


def translate_speech_mic_speaker():
   # Get user input
    targetLanguage = ''
    targetLanguage = input('\nEnter a target language\n fr = French\n es = Spanish\n hi = Hindi\n Enter anything else to stop\n').lower()
    if targetLanguage not in translation_config.target_languages:
        return
    
    print('Translating to', targetLanguage)

    translation = translate_from_mic(targetLanguage)
    if not translation:
        return  
    
    # Synthesize translation to speaker
    voices = {
            "fr": "fr-FR-HenriNeural",
            "es": "es-ES-ElviraNeural",
            "hi": "hi-IN-MadhurNeural"
    }
    speech_config.speech_synthesis_voice_name = voices.get(targetLanguage)
    audio_config_out = speech_sdk.audio.AudioOutputConfig(use_default_speaker=True)
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config, audio_config_out)
    speak = speech_synthesizer.speak_text_async(translation).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)


if __name__ == "__main__":
    main()