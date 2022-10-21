from collections import OrderedDict


class Flowers:

    def __init__(self, name, freshness, color, stem_length, price, life_time):
        self.name = name
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length
        self.price = price
        self.life_time = life_time


class Bouquet:

    def __init__(self):
        self.flowers = list()
        self.total_price = list()
        self.bouquet_life_time = list()

    def add_to_bouquet(self, flowers):
        for flower in flowers:
            self.flowers.append(flower)
            self.total_price.append(flower.price)
            self.bouquet_life_time.append(flower.life_time)

    def get_bouquet_price(self):
        return sum(self.total_price)

    def get_bouquet_life_time(self):
        return sum(self.bouquet_life_time) / len(self.bouquet_life_time)

    def check_if_exist(self, flower):
        return True if flower.name in self.flowers else False

    def find_in_bouquet_by_param(self, **kwargs):
        for flower in self.flowers:
            if all([getattr(flower, k) == v for k, v in kwargs.items()]):
                return getattr(flower, 'name')

    def sort_bouquet_by_param(self, param):
        return OrderedDict(sorted({getattr(flower, param): flower.name for flower in self.flowers}.items())).values()
