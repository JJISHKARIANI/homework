import json
from models import Joke

class Storage:
    FILENAME = "jokes_history.json"

    @classmethod
    def load_joke(cls):
        try:
            with open(cls. FILENAME, "r", encoding='utf-8') as file:
                data = json.load(file)
                return [Joke.from_dict(i) for i in data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    @classmethod
    def save_joke(cls, jokes_list):
        try:
            with open(cls.FILENAME, "w", encoding='utf-8') as file:
                data = [i.to_dict() for i in jokes_list]
                json.dump(data, file, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"[error]: {e}")


    @classmethod
    def add_joke(cls, joke: Joke):
        jokes = cls.load_joke()
        jokes.append(joke)
        cls.save_joke(jokes)


    @classmethod
    def delete_joke(cls, index: int):
        jokes = cls.load_joke()
        if 0 <= index < len(jokes):
            jokes.pop(index)
            cls.save_joke(jokes)
            return True
        return False
