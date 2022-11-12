from datetime import datetime
from datetime import timedelta


class Flower:

    def __init__(self, name, color, cut_flower_date, lifetime, amount, cost_price):
        self.name = name
        self.color = color
        self.cut_flower_date = cut_flower_date
        self.lifetime = lifetime
        self.amount = amount
        self.cost_price = cost_price
        self.total_price = cost_price
        self.sale = 0


class Rose(Flower):
    def __init__(self, name, color, stem_length, cut_flower_date, lifetime, amount, cost_price):
        super(Rose, self).__init__(name, color, cut_flower_date, lifetime, amount, cost_price)
        self.stem_length = stem_length


class Peony(Flower):
    def __init__(self, name, color, cut_flower_date, lifetime, amount, cost_price):
        super(Peony, self).__init__(name, color, cut_flower_date, lifetime, amount, cost_price)


class Lilies(Flower):
    def __init__(self, name, color, cut_flower_date, lifetime, amount, cost_price):
        super(Lilies, self).__init__(name, color, cut_flower_date, lifetime, amount, cost_price)


class Shop:
    def __init__(self, trade_margin):
        self.trade_margin = trade_margin
        self.flowers = list()
        self.bouquet = list()

    def add_flower(self, flower):
        self.flowers.append(flower)

    def collect_bouquet_of_flowers(self):
        names = set()
        colors = set()
        x = "y"
        while x == "y":

            [names.add(flower.name) for flower in self.flowers]
            name = input(f"Choose a flower {names}:\n")

            [colors.add(flower.color) for flower in self.flowers if name == flower.name]
            color = input(f"Choose the color of the {name}: {colors}\n")

            cost_prices = [flower.cost_price for flower in self.flowers if
                           name == flower.name and color == flower.color]

            total_prices = [cost_price + cost_price * self.trade_margin for cost_price in cost_prices]
            total_price = int(input(f"Choose the price: {total_prices}\n"))
            amount = int(input("Enter amount:\n"))

            for flower in self.flowers:
                flower.total_price = total_price
                if name == flower.name and color == flower.color \
                        and flower.total_price == flower.cost_price + flower.cost_price * self.trade_margin:
                    self.add_flower_to_bouquet(flower, amount)
                    print(flower)
                continue
            total_prices.clear()
            cost_prices.clear()
            colors.clear()
            x = input("Should you wish to continue? y/n\n")
        print(self.bouquet)
        print(len(self.bouquet))

    def add_flower_to_bouquet(self, flower, amount):
        flower.amount -= amount
        for _ in range(amount):
            self.bouquet.append(flower)

    def get_total_price_of_bouquet_of_flowers(self):
        cost_of_bouquet = sum(flower.cost_price for flower in self.bouquet)
        return cost_of_bouquet + (cost_of_bouquet * self.trade_margin)

    def get_wither_time_of_bouquet(self):
        wither_time = 0
        assert len(self.bouquet) > 0, IndexError
        for flower in self.bouquet:
            begin_date = datetime.strptime(flower.cut_flower_date, '%d/%m/%Y')
            end_date = begin_date + timedelta(days=flower.lifetime)
            wither_time += (end_date - datetime.now()).days
        return int(wither_time / len(self.bouquet))

    def sort_flowers_in_bouquet(self, param):
        return sorted(self.bouquet, key=lambda flower: getattr(flower, param))

    def search_for_flowers_in_bouquet(self, **parameters):
        result = list()
        for key, parameter in parameters.items():
            for flower in self.bouquet:
                if key == 'name' and parameter == getattr(flower, 'name'):
                    result.append(flower)
                    continue
                elif key == 'color' and parameter == getattr(flower, 'color'):
                    result.append(flower)
                    continue
                elif key == 'lifetime' and parameter == getattr(flower, 'lifetime'):
                    result.append(flower)
                    continue
                elif key == 'amount' and parameter == getattr(flower, 'amount'):
                    result.append(flower)
                    continue
                elif key == 'cost_price' and parameter == getattr(flower, 'cost_price'):
                    result.append(flower)
                    continue
        if len(result) > 0:
            print(f"Your search returned {len(result)} results:")
            print(set(result))
        else:
            print("Nothing found for your request")

    def is_exist_flower_in_bouquet(self, name):
        print(f"Does the bouquet contain {name}? "
              + str(bool(any(name in getattr(flower, 'name') for flower in self.bouquet))))


shop = Shop(1)

rose_50 = Rose("Rose", "Red", 50, "18/10/2022", 7, 100, 100)
rose_60 = Rose("Rose", "Blue", 60, "19/10/2022", 7, 100, 110)
rose_70 = Rose("Rose", "Yellow", 70, "20/10/2022", 7, 100, 120)
peony = Peony("Peony", "Pink", "17/10/2022", 7, 100, 130)

shop.add_flower(rose_50)
shop.add_flower(rose_60)
shop.add_flower(rose_70)
shop.add_flower(peony)

shop.collect_bouquet_of_flowers()
print("For payment:", shop.get_total_price_of_bouquet_of_flowers())
print("The bouquet will last an average of than", shop.get_wither_time_of_bouquet(), "days.")
print(shop.sort_flowers_in_bouquet("color"))

shop.search_for_flowers_in_bouquet(name="Rose", color="Pink", lifetime=0, amount=0, cost_price=0)
shop.is_exist_flower_in_bouquet("Rose")
