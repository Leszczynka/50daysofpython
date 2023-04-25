from abc import ABC
"""
Day 41: Only Words with Vowels.
Create a function called words_with_vowels, this function takes a string of words and returns a list of only words
that have vowels on them. For example 'You have no rhythm' should return ['You', 'have', 'no'].
"""


def words_with_vowels(words: str) -> list:
    return [word for word in words.split() if any(char in 'aeiou' for char in word)]


"""
Extra Challenge: Class of Cars.
Create three classes of three car brands - Ford, BMW and Tesla. The attributes of the car's objects will be:
model, color, year, transmission and whether the car is electric or not (Boolean value).
Consider using inheritance in your answer. You will create one object for each car brand:
bmw1: model: x6, color: silver, year: 2018, transmission: auto, electric: False
tesla1: model: S, color: beige, year: 2017, transmission: auto, electric: True
ford1: model: focus, color: white, year: 2020, transmission: auto, electric: False
You will create a class method called print_cars that will be able to print out objects of the class. For example,
if you call the method on the ford1 object of the Ford class,
your function should be able to print out car info in this exact format:
car_model=focus
color=white
year=2020
transmission=auto
electric=False
"""


class Car(ABC):
    def __init__(self, model, color, year, transmission, electric):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric

    def print_cars(self):
        print(f'car_model={self.model}\ncolor={self.color}\nyear={self.year}\ntransmission={self.transmission}\nelectric={self.electric}')


class Ford(Car):
    def __init__(self, model, color, year, transmission, electric):
        super().__init__(model, color, year, transmission, electric)


class BMW(Car):
    def __init__(self, model, color, year, transmission, electric):
        super().__init__(model, color, year, transmission, electric)


class Tesla(Car):
    def __init__(self, model, color, year, transmission, electric):
        super().__init__(model, color, year, transmission, electric)


if __name__ == '__main__':
    print(words_with_vowels('You have no rhythm'))

    bmw = BMW(model='x6', color='silver', year=2018, transmission='auto', electric=False)
    bmw.print_cars()

    tesla = Tesla(model='S', color='beige', year=2017, transmission='auto', electric=True)
    tesla.print_cars()

    ford = Ford(model='focus', color='white', year=2020, transmission='auto', electric=False)
    ford.print_cars()
