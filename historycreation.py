
history = []
def create_history(role: str, parts: str):
    obj = {
        "role": role,
        "parts": [
            parts
        ]
    }
    history.append(obj)