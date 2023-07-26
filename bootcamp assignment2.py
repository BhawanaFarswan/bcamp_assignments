class Animal:
    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):
    def make_sound(self):
        super().make_sound()  # Call base class's make_sound() method
        print("Bark")


class Cat(Animal):
    def make_sound(self):
        super().make_sound()  # Call base class's make_sound() method
        print("Meow")


def animal_sound_in_zoo(animal):
    animal.make_sound()


def main():
    dog = Dog()
    cat = Cat()

    print("Dog sound in the zoo:")
    animal_sound_in_zoo(dog)

    print("\nCat sound in the zoo:")
    animal_sound_in_zoo(cat)


if __name__ == "__main__":
    main()
