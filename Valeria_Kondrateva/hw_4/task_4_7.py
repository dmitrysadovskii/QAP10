from collections import Counter


def find_frequent_letter(text):
    text = str(text).lower()
    ct = Counter(text)
    most_commons = ct.most_common(1)
    most_frequent = most_commons[0]
    return most_frequent[0]


if __name__ == "__main__":
    r = find_frequent_letter("HelLo WorLd! How do you do? Oops!")
    print(r)
