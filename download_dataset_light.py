from datasets import load_dataset
import os
import soundfile as sf
import numpy as np

# Load the dataset
dataset = load_dataset("benax-rw/my_kinyarwanda_dataset", split="train")

# Ensure output directory exists
os.makedirs("audio", exist_ok=True)
transcription_file = open("audio/transcriptions.txt", "w", encoding="utf-8")

print("⬇️ Downloading first 5 samples...")

for i in range(5):
    sample = dataset[i]
    audio_array = np.array(sample["audio"]["array"])
    sample_rate = sample["audio"]["sampling_rate"]
    text = sample["text"]

    # Save .wav file
    file_path = f"audio/question{i+1}.wav"
    sf.write(file_path, audio_array, sample_rate)
    
    # Save transcription
    transcription_file.write(f"{file_path}: {text}\n")
    print(f"✅ Saved {file_path}")

transcription_file.close()
print("🎉 Done! Audio saved in 'audio/' and transcriptions in 'transcriptions.txt'")
