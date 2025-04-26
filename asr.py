from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torchaudio

model = WhisperForConditionalGeneration.from_pretrained("benax-rw/KinyaWhisper")
processor = WhisperProcessor.from_pretrained("benax-rw/KinyaWhisper")

def transcribe(audio_path):
    waveform, sample_rate = torchaudio.load(audio_path)
    inputs = processor(waveform.squeeze(), sampling_rate=sample_rate, return_tensors="pt")
    predicted_ids = model.generate(inputs["input_features"])
    return processor.batch_decode(predicted_ids, skip_special_tokens=True)[0].lower()
