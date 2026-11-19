from InvalidGradeError import InvalidGradeError


class Student:
    def __init__(self, name, grade=0):
        self.name = name
        self.grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        if grade > 100 or grade < 0:
            raise InvalidGradeError(f"Grade must be between 0 and 100, given: {grade}")
        self._grade = grade

    @staticmethod
    def is_passing(grade):
        return grade >= 50

    @classmethod
    def from_string(cls, text):
        parts = text.split("-")
        if len(parts) == 2 and parts[1].isdigit():
            return cls(parts[0], int(parts[1]))
        else:
            raise ValueError("Wrong input format, input must be like this : 'name-grade'. Huseyn-85")

    def __str__(self):
        return f"{self.name} | {self.grade} | {"Passed" if self.is_passing(self.grade) else "Failed"}"
