import speech_recognition as sr
from langdetect import detect
import pyaudio

recognizer = sr.Recognizer()

def detect_language_from_audio():
    with sr.Microphone() as source:
        print("Ajustando para o ruído ambiente...")
        recognizer.adjust_for_ambient_noise(source)
        print("Por favor, fale agora...")

        # Captura o áudio do microfone
        audio = recognizer.listen(source)

        try:
            # Usa a API do Google para transcrever o áudio para texto
            text = recognizer.recognize_google(audio)
            print(f"Texto reconhecido: {text}")

            # Detecta o idioma do texto transcrito
            language = detect(text)
            print(f"Idioma detectado: {language}")

        except sr.UnknownValueError:
            print("Não foi possível reconhecer o áudio.")
        except sr.RequestError:
            print("Erro ao conectar com o serviço de reconhecimento de fala.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    detect_language_from_audio()
