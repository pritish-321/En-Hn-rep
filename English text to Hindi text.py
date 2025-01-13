import pyttsx3
from googletrans import Translator

def translate_and_speak(text, target_language="hi"):
    """
    Translate English text to the target language and speak it aloud.
    
    Parameters:
        text (str): The English text to be translated.
        target_language (str): The target language code (default: 'hi' for Hindi).
    """
    # Initialize the translator
    translator = Translator()
    
    try:
        # Translate the text
        translation = translator.translate(text, src="en", dest=target_language)
        translated_text = translation.text
        
        print(f"Original Text: {text}")
        print(f"Translated Text: {translated_text}")
        
        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        
        # Set properties for the Hindi voice (check available voices on your system)
        voices = engine.getProperty('voices')
        for voice in voices:
            if 'hindi' in voice.name.lower():
                engine.setProperty('voice', voice.id)
                break
        else:
            print("Hindi voice not found. Using default voice.")
        
        # Speak the translated text
        engine.say(translated_text)
        engine.runAndWait()
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input English text
    english_text = input("Enter the English text to translate: ")
    
    # Translate to Hindi and speak
    translate_and_speak(english_text)
