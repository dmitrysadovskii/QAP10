class Flower():
    def __init__(self, kind, color, length, price, freshness=0):
        self.kind = kind
        self.color = color
        self.freshness = freshness
        self.length = length
        self.price = price

    def __str__(self):
        return f'{self.kind: <10}{self.color: <10}{str(self.freshness) + " days": <15}\
            "{str(self.length * 100) + "cm": <10}{str(self.price) + "$": <5}'""


class Bouquet():
    def __init__(self, flowers=[]):
        self.flowers = flowers
        if flowers:
            self.total_price = sum([flower_x.price for flower_x in self.flowers])
        else:
            self.total_price = 0

    def __contains__(self, flower_x):
        return flower_x in self.flowers

    def add_flowers(self, *new_flowers):
        self.flowers += new_flowers
        self.total_price = sum([flower_x.price for flower_x in self.flowers])

    def avg_lifetime(self):
        from statistics import mean
        if self.flowers:
            return f'{round(mean([flower_x.freshness for flower_x in self.flowers]), 2)} days of average lifetime'
        else:
            return 'The Bouquet is empty by now!'

    def describe(self):
        print('Bouquets flowers description:\n')
        print(f'{"Kind": <10}{"Color": <10}{"Freshness": <15}{"Length": <8}{"Price": <5}\n')
        for flower in self.flowers:
            print(flower)
        print('\n')

    def sort_bouquet(self, key='price'):
        if key == 'price':
            self.flowers.sort(key=lambda flower: flower.price)
        elif key == 'color':
            self.flowers.sort(key=lambda flower: flower.color)
        elif key == 'length':
            self.flowers.sort(key=lambda flower: flower.length)
        elif key == 'freshness':
            self.flowers.sort(key=lambda flower: flower.freshness)
        print('Произошла сортировка букета по ', key)


rose = Flower('Rose', 'Red', 0.2, 2, freshness=3)
lily = Flower('Lily', 'Pink', 0.16, 1.5)
tulip = Flower('Tulip', 'Yellow', 0.15, 1, freshness=1)
rose2 = Flower('Rose', 'White', 0.3, 10, freshness=14)

B1 = Bouquet(flowers=[rose])
B1.add_flowers(lily, tulip)
B1.sort_bouquet(key='freshness')
B1.describe()
print(B1.avg_lifetime())
print(B1.total_price)
print(rose in B1, rose2 in B1)
