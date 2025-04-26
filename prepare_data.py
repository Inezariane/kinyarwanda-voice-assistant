import torchaudio
import torch
from datasets import load_dataset
import os
import json

# Create audio folder
os.makedirs("audio", exist_ok=True)

# Load dataset
ds = load_dataset("benax-rw/my_kinyarwanda_dataset", split="train")

qa_dict = {}

# Save first 5 examples
for i in range(5):
    audio_array = torch.tensor(ds[i]["audio"]["array"])
    sample_rate = ds[i]["audio"]["sampling_rate"]

    filename = f"audio/sample{i+1}.wav"
    torchaudio.save(filename, audio_array.unsqueeze(0), sample_rate)

    question_text = ds[i]["text"].strip().lower()
    print(f" Saved {filename} — Q: {question_text}")

    # Auto-answer (customize later if you want)
    qa_dict[question_text] = f"Iki ni igisubizo cya '{question_text}'."

# Save qa_dict as JSON
with open("qa_dict.json", "w", encoding="utf-8") as f:
    json.dump(qa_dict, f, ensure_ascii=False, indent=2)

print("\n All audio saved. Q&A dictionary written to qa_dict.json!")
