class Student:
    def __init__(self, name: str, roll_number: int, grade: float):
        self._name = name
        self._roll_number = roll_number
        self._grade = grade

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("name cannot be space")
        self._name = value

    @property
    def roll_number(self) -> int:
        return self._roll_number

    @property
    def grade(self) -> float:
        return self._grade

    @grade.setter
    def grade(self, value: float):
        if not (0.0 <= value <= 100.0):
            raise ValueError("a grade must be number from 0.0 to 100.0")
        self._grade = value

    def __repr__(self) -> str:
        return f"student(name={self._name}, roll_number={self._roll_number}, grade={self._grade})"

    def __str__(self) -> str:
        return f"Student: name: {self._name}, roll_number: {self._roll_number}, grade: {self._grade}"