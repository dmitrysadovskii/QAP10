"""
Цветочница.
Определить иерархию и создать несколько цветов. Собрать букет (можно
использовать аксессуары) с определением его стоимости.
Определить время его увядания по среднему времени жизни всех цветов в букете.
Позволить сортировку цветов в букете на основе различных параметров
(свежесть/цвет/длина стебля/стоимость...)
Реализовать поиск цветов в букете по определенным параметрам.
Узнать, есть ли цветок в букете.
"""
class Flower:

    def __init__(self, color, price, length, lifetime):
        self.color = color
        self.price = price
        self.length = length
        self.lifetime = lifetime

    def __repr__(self):
        return f"{self.color} {self.__class__.__name__}"




class Hydrangea(Flower):

    def __init__(self, color, price, length, lifetime):
        super().__init__(color, price, length, lifetime)

    @property
    def price(self):
        return self.price


class Eustoma(Flower):

    def __init__(self, color, price, length, lifetime):
        super().__init__(color, price, length, lifetime)


class Carnation(Flower):

    def __init__(self, color, price, length, lifetime):
        super().__init__(color, price, length, lifetime)


class Eucalyptus(Flower):

    def __init__(self, color, price, length, lifetime):
        super().__init__(color, price, length, lifetime)


class Bouquet:

    def __init__(self, *flowers):
        self.flower_list = [i for i in flowers]
        price = sum([i.price for i in flowers])
        lifetime = sum([i.lifetime for i in flowers]) / len(flowers)

    def sort_flowers_by_price(self):
        return


flower = Hydrangea("blue", 100, 100, 5)
print(flower.price)