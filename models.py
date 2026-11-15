class Joke:
    def __init__(self, category: str, type: str, joke: str = None, setup: str = None, delivery: str = None):
        self.category = category
        self.type = type
        self.joke = joke
        self.setup = setup
        self.delivery = delivery


    def to_dict(self):
        return {
            "category": self.category,
            "type": self.type,
            "joke": self.joke,
            "setup": self.setup,
            "delivery": self.delivery
        }
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            category=data.get("category"),
            type=data.get("type"),
            joke=data.get("joke"),
            setup=data.get("setup"),
            delivery=data.get("delivery")
        )

    def display(self):
        print(f"category: {self.category}")
        if self.joke ==  "single":
            print(f"joke: {self.joke}")
        else:
            print(f"setup: {self.setup}") 
            print(f"delivery: {self.delivery}") 




