from asr import transcribe
from nlp import get_answer
from tts import speak

def run_assistant(audio_file):
    print("Transcribing...")
    question = transcribe(audio_file)
    print("You said:", question)

    response = get_answer(question)
    print("Responding with:", response)

    speak(response)

if __name__ == "__main__":
    run_assistant("audio/sample1.wav")
