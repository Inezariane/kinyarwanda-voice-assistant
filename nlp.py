import json

# Load the dictionary
with open("qa_dict.json", "r", encoding="utf-8") as f:
    qa_dict = json.load(f)

def get_answer(text):
    return qa_dict.get(text.lower(), "Ndasubiramo, sinabyumvise neza.")
