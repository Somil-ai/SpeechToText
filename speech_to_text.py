import speech_recognition as sr

def transcribe_audio(audio_file_path):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    try:
        # Load audio file
        with sr.AudioFile(audio_file_path) as source:
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source)
            
            # Listen to audio
            audio = recognizer.listen(source)
            
            # Transcribe using Google's Speech Recognition API
            text = recognizer.recognize_google(audio)
            return text
            
    except sr.UnknownValueError:
        return "Could not understand the audio"
    except sr.RequestError as e:
        return f"Could not request results; {e}"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    # Example usage
    audio_file = "sample.wav"  # Replace with your audio file path
    result = transcribe_audio(audio_file)
    print("Transcription:", result)

if __name__ == "__main__":
    main()