class Flower:
    def __init__(self, name, color, stem_length, cost, lifespan):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.cost = cost
        self.lifespan = lifespan

    def __repr__(self):
        return f"{self.name}"


class Bouquet:
    def __init__(self, flowers=None):
        if flowers is None:
            flowers = []
        self.flowers = flowers

    def add_flower(self, flower):
        self.flowers.append(flower)

    def fading_time(self):
        total_lifespan = sum([flower.lifespan for flower in self.flowers])
        avg_lifespan = total_lifespan / len(self.flowers)
        return round(avg_lifespan)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda x: x.lifespan, reverse=True)

    def sort_by_color(self):
        self.flowers.sort(key=lambda x: x.color)

    def sort_by_stem_length(self):
        self.flowers.sort(key=lambda x: x.stem_length, reverse=True)

    def sort_by_cost(self):
        self.flowers.sort(key=lambda x: x.cost)

    def search_by_color(self, color):
        return [flower for flower in self.flowers if flower.color == color]

    def search_by_stem_length(self, length):
        return [flower for flower in self.flowers if flower.stem_length >= length]

    def search_by_cost(self, cost):
        return [flower for flower in self.flowers if flower.cost <= cost]

    def has_flower(self, name):
        return any(flower.name == name for flower in self.flowers)


lavender = Flower("Lavender", "purple", 20, 2, 5)
poppy = Flower("Poppy", "red", 15, 3, 4)
cornflower = Flower("Cornflower", "blue", 18, 1, 6)

bouquet = Bouquet([lavender, poppy, cornflower])
print("Fading time:", bouquet.fading_time(), "days")

total_cost = sum([flower.cost for flower in bouquet.flowers])
print("Cost of bouquet:", total_cost)

has_flower = bouquet.has_flower("Rose")
print("Has Rose:", has_flower)

bouquet.sort_by_freshness()
print("Sorted by freshness:", ", ".join([flower.name for flower in bouquet.flowers]))

bouquet.sort_by_color()
print("Sorted by color:", ", ".join([flower.name for flower in bouquet.flowers]))

bouquet.sort_by_stem_length()
print("Sorted by stem length:", ", ".join([flower.name for flower in bouquet.flowers]))

bouquet.sort_by_cost()
print("Sorted by cost:", ", ".join([flower.name for flower in bouquet.flowers]))

print("Purple flowers in bouquet:", ", ".join([flower.name for flower in bouquet.search_by_color("purple")]))
