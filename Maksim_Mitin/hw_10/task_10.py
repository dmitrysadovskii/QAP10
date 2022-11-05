class Flower:
    def __init__(self, freshness, color, length, cost, name):
        self.freshness = freshness
        self.color = color
        self.length = length
        self.cost = cost
        self.name = name


class Rose(Flower):
    def __init__(self, freshness=5, color="Pink", length=20, cost=30, name="Rose"):
        super().__init__(freshness, color, length, cost, name)


class Orchid(Flower):
    def __init__(self, freshness=7, color="Purple and White", length=10, cost=50, name="Orchid"):
        super().__init__(freshness, color, length, cost, name)


class Carnation(Flower):
    def __init__(self, freshness=10, color="Red", length=8, cost=20, name="Carnation"):
        super().__init__(freshness, color, length, cost, name)


class Peon(Flower):
    def __init__(self, freshness=6, color="White", length=12, cost=4, name="Peon"):
        super().__init__(freshness, color, length, cost, name)


class Tulip(Flower):
    def __init__(self, freshness=3, color="Yellow", length=8, cost=36, name="Tulip"):
        super().__init__(freshness, color, length, cost, name)


class Bouquet:
    def __init__(self):
        self.bouquet = []

    def add_flower(self, flower):
        self.bouquet.append(flower)

    def total_flowers_in_bouquet(self):
        return len(self.bouquet)

    def price_total(self):
        price = 0
        for flower in self.bouquet:
            price = price + flower.cost
        return price

    def average_freshness(self):
        return sum([flower.freshness for flower in self.bouquet])

    def find_color_in_bouquet(self, color):
        return [flower.name for flower in self.bouquet if flower.color == color]

    def find_length_in_bouquet(self, length):
        return [flower.name for flower in self.bouquet if flower.length == length]

    def find_cost_in_bouquet(self, cost):
        return [flower.name for flower in self.bouquet if flower.cost == cost]

    def sort_by_cost(self):
        sorted_list = sorted(self.bouquet, key=lambda flower: flower.cost)
        print([flower.name for flower in sorted_list])

    def sort_by_length(self):
        sorted_list = sorted(self.bouquet, key=lambda flower: flower.length)
        print([flower.name for flower in sorted_list])

    def sort_by_freshness(self):
        sorted_list = sorted(self.bouquet, key=lambda flower: flower.freshness)
        print([flower.name for flower in sorted_list])


flower_1 = Rose()
flower_2 = Rose()
flower_3 = Orchid()
flower_4 = Peon()
flower_5 = Tulip()
flower_6 = Carnation()

print(flower_1.freshness)
print(flower_5.color)

bouquet = Bouquet()

bouquet.add_flower(flower_1)
bouquet.add_flower(flower_2)
bouquet.add_flower(flower_3)
bouquet.add_flower(flower_4)
bouquet.add_flower(flower_5)
bouquet.add_flower(flower_6)

print(bouquet.total_flowers_in_bouquet())
print(bouquet.price_total())
print(bouquet.find_color_in_bouquet('Red'))
print(bouquet.find_length_in_bouquet(10))
print(bouquet.find_cost_in_bouquet(36))
bouquet.sort_by_cost()
bouquet.sort_by_length()
bouquet.sort_by_freshness()
