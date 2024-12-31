
history = []
def create_history(role: str, parts: str):
    obj = {
        "role": role,
        "parts": [
            parts
        ]
    }
    history.append(obj)

def find_in_history(word: str):
    for i, obj in enumerate(history):
        if obj["role"] == "user" and obj["parts"][0].lower() == word.lower():
            return "".join(history[i+1]["parts"])
