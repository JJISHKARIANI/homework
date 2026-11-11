class Joke:
    def __init__(self, category: str, joke_type: str, joke: str = None, setup: str = None, delivery: str = None):
        self.category = category
        self.joke_type = joke_type
        self.joke = joke
        self.setup = setup
        self.delivery = delivery

    def to_dict(self):
        """ლექსიკონში გარდაქმნა JSON-ში შესანახად"""
        return {
            "category": self.category,
            "type": self.joke_type,
            "joke": self.joke,
            "setup": self.setup,
            "delivery": self.delivery
        }

    @classmethod
    def from_dict(cls, data: dict):
        """JSON ლექსიკონიდან ობიექტის შექმნა"""
        return cls(
            category=data.get("category"),
            joke_type=data.get("type"),
            joke=data.get("joke"),
            setup=data.get("setup"),
            delivery=data.get("delivery")
        )

    def display(self):
        print(f"\n📂 კატეგორია: {self.category}")
        if self.joke_type == 'single':
            print(f"💬 ხუმრობა: {self.joke}")
        else:
            print(f"❓ სეტაპი: {self.setup}")
            print(f"💡 პასუხი: {self.delivery}")



