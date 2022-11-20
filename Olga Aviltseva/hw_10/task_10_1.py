class Flower:
    __name: str
    __color: str
    __lifetime: int
    __stem_length: int
    __price: int

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color

    @property
    def lifetime(self):
        return self.__lifetime

    @property
    def stem_length(self):
        return self.__stem_length

    @property
    def price(self):
        return self.__price

    def __init__(self, name, color, lifetime, stem_length, price):
        self.__name = name
        self.__color = color
        self.__lifetime = lifetime
        self.__stem_length = stem_length
        self.__price = price


class Rose(Flower):
    def __init__(self, name="Rose", color="Red", lifetime=7, stem_length=30, price=3):
        super().__init__(name, color, lifetime, stem_length, price)


class Gladiolus(Flower):
    def __init__(self, name="Gladiolus", color="Yellow", lifetime=5, stem_length=50, price=2):
        super().__init__(name, color, lifetime, stem_length, price)


class Pion(Flower):
    def __init__(self, name="Pion",  color="White", lifetime=3, stem_length=20, price=1):
        super().__init__(name, color, lifetime, stem_length, price)


class Bouquet:

    def __init__(self, *flower):
        self.__bouquet = list(flower)

    def add_flower(self, flower):
        self.__bouquet.append(flower)

    @property
    def price(self):
        return sum([flower.price for flower in self.__bouquet])

    def average_lifetime(self):
        return sum([flower.lifetime for flower in self.__bouquet]) / len(self.__bouquet)

    def find_color_in_bouquet(self, color):
        return [flower.name for flower in self.__bouquet if flower.color.upper() == color.upper()]

    def find_length_in_bouquet(self, length):
        return [flower.name for flower in self.__bouquet if flower.stem_length == length]

    def sort_by_cost(self):
        sorted_list = sorted(self.__bouquet, key=lambda flower: flower.price * (-1))
        print(*[flower.name for flower in sorted_list])

    def sort_by_length(self):
        sorted_list = sorted(self.__bouquet, key=lambda flower: flower.stem_length)
        print(*[flower.name for flower in sorted_list])

    def sort_by_freshness(self):
        sorted_list = sorted(self.__bouquet, key=lambda flower: flower.lifetime)
        print(*[flower.name for flower in sorted_list])


flower_1 = Rose()
flower_2 = Gladiolus()
flower_3 = Pion()

bouquet = Bouquet()

bouquet.add_flower(flower_1)
bouquet.add_flower(flower_2)
bouquet.add_flower(flower_3)
print(bouquet.price)

greenFlowers = bouquet.find_color_in_bouquet('Red')
if len(greenFlowers) > 0:
    print(*greenFlowers)
else:
    print("No flowers were found")

print(bouquet.find_length_in_bouquet(20))

bouquet.sort_by_cost()
bouquet.sort_by_length()
bouquet.sort_by_freshness()

print(bouquet.average_lifetime())
