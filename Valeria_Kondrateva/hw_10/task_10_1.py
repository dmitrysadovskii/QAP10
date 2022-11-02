class Flower:
    def __init__(self, name, color, freshness_time, stem_length, price):
        self.name = name
        self.color = color
        self.freshness_time = freshness_time
        self.stem_length = stem_length
        self.price = price

    def __str__(self):
        print(f"Название - {self.name}, Цвет - {self.color}, Свежесть - {self.freshness_time}, "
              f"Длинна - {self.stem_length}, Цена - {self.price}")


class Rose(Flower):
    def __init__(self, name, color, freshness_time, stem_length, price):
        super().__init__(name, color, freshness_time, stem_length, price)


class Tulip(Flower):
    def __init__(self, name, color, freshness_time, stem_length, price):
        super().__init__(name, color, freshness_time, stem_length, price)


class Chamomile(Flower):
    def __init__(self, name, color, freshness_time, stem_length, price):
        super().__init__(name, color, freshness_time, stem_length, price)


def freshness(bouquet):
    new_list = []
    for i in bouquet.content:
        new_list.append(i.freshness_time)

    return sum(list(set(new_list))) / len(list(set(new_list)))


def sorte(lst):
    global new_lst
    param = int(input("По чем фильтровать?\n"
                      "1 - свежесть\n"
                      "2 - цвет\n"
                      "3 - длинна стебля\n"
                      "4 - цена\n"))
    if param == 1:
        new_lst = sorted(lst, key=lambda x: x.freshness_time)
    elif param == 2:
        new_lst = sorted(lst, key=lambda x: x.color)
    elif param == 3:
        new_lst = sorted(lst, key=lambda x: x.stem_length)
    elif param == 4:
        new_lst = sorted(lst, key=lambda x: x.price)
    else:
        print("Такого фильтра нет.")
    return new_lst


def fun(bouq, flow):
    for i in bouq:
        if i.name == flow:
            return "Цветок есть в букете"


rose_red = Rose("Роза", "Красный", 2, 50, 5)
tulip = Tulip("Тюльпан", "Желтый", 3, 40, 2.5)
chamomile = Chamomile("Ромашка", "Белый", 10, 30, 3)

my_buq = [rose_red, rose_red, tulip, chamomile]


print(f"Стоимость букета {sum(i.price for i in my_buq)} руб.")
print(f"Засохнет через {sum([i.freshness_time for i in my_buq]) / len([i.freshness_time for i in my_buq])} ч.")
print(fun(my_buq, "Роза"))


for i in my_buq:
    i.__str__()

my_buq = sorte(my_buq)

for i in my_buq:
    i.__str__()


def search(lst):
    search_color = input("Введите нужный цвет ")
    search_freshness_time = input("Введите нужную свежесть ")
    search_stem_length = input("Введите нужную длинну ")
    search_price = input("Введите нужную цену ")

    new_lst_sear = []

    for i in lst:
        if i.color == search_color or search_color == "":
            if str(i.freshness_time) == search_freshness_time or search_freshness_time == "":
                if str(i.stem_length) == search_stem_length or search_stem_length == "":
                    if str(i.price) == search_price or search_price == "":
                        new_lst_sear.append(i)
    return new_lst_sear


print(search(my_buq))
