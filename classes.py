class Animal(object):
    def __init__(self, name, weight, voice):
        self.name = name
        self.weight = weight
        self.voice = voice

    def feed(self):
        # кормить
        print('Feed', self.name)

    def voice(self):
        # различать по голосам
        print('voice', self.name, self.voice)


class Sheep(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'beeeee')

    def shave(self):
        # овец стричь
        print('Shave', self.name)

    def product(self):
        self.shave()


class MilkyAnimal(Animal):
    def milk(self):
        # корову и коз доить
        print('Get milk from', self.name)

    def product(self):
        self.milk()


class Cow(MilkyAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'mooo')


class Goat(MilkyAnimal):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'meee')


class Bird(Animal):
    def __init__(self, name, weight, voice):
        super().__init__(name, weight, voice)

    def egg(self):
        # собирать яйца у кур, утки и гусей
        print('Get eggs from', self.name)

    def product(self):
        self.egg()


class Goose(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'honk')


class Chicken(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'kudah')


class Duck(Bird):
    def __init__(self, name, weight):
        super().__init__(name, weight, 'krya')


goose_1 = Goose('Gray', 5.2)
goose_2 = Goose('White', 6.1)
cow = Cow("Manyka", 170.5)
sheep_1 = Sheep('Barashek', 25.6)
sheep_2 = Sheep('Kydraviy', 24.7)
chicken_1 = Chicken('KoKo', 2.5)
chicken_2 = Chicken('Kukareku', 3.5)
goat_1 = Goat('Roga', 26.8)
goat_2 = Goat('Kopyta', 17)
duck = Duck('Kryakva', 5)

animals = [goose_1, goose_2, cow, sheep_1, sheep_2, chicken_1, chicken_2, goat_1, goat_2, duck]

print('feed animals\n')
for animal in animals:
    animal.feed()
print('\ninteraction with animals:\n')
for animal in animals:
    animal.product()

total_weight = sum(animal.weight for animal in animals)
print("Общий вес животных равен:", total_weight, "кг")

heaviest_animal = None
# поиск наиболее тяжелого животного
for animal in animals:
    if heaviest_animal is None:
        heaviest_animal = animal
    elif animal.weight > heaviest_animal.weight:
        heaviest_animal = animal
print('Самое тяжелое животное это:', heaviest_animal.name)