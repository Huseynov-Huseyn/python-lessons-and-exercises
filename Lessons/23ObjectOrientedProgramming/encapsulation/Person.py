# Encapsulation profits:
# Data Protection: Prevents accidental modification of data
# Validation: You can validate data before setting it
# Flexibility: Internal implementation can change without affecting external code
# Control: You have full control over how data is accessed and modified


class Person:
    birth_year = 0

    def __init__(self, name, age, surname):
        self.name = name
        # private property = cannot call from another classes
        self.__age = age
        # protected property =  called from another classes, but you shouldn't
        self._surname = surname
        self.birth_year = self.__calculate_birth_year(age)

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

    def __calculate_birth_year(self, age):
        return 2026 - age
