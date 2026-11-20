from Animal import Animal
from Bird import Bird
from Cat import Cat
from Dog import Dog


def main():
    try:
        animal1 = Animal("Husky", 21)
    except Exception as e:
        print(e)
    finally:
        print("Done.")

    try:
        dog1 = Dog("Rex", -1)
    except ValueError as e:
        print(e)
    finally:
        print("Done.")

    try:
        dog1 = Dog("Rex", 8)
        cat1 = Cat("Ginger", 3)
        bird1 = Bird("Coco", 2, True)
        animals = [dog1, cat1, bird1]
        for animal in animals:
            print(animal.describe())
        print(dog1 == cat1)
        print(dog1 > cat1)
        print(dog1 + cat1)
    except Exception as e:
        print(e)
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
