import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


class passwordGenerator:
    def generate_password(self):

        letters_list = [random.choice(letters) for i in range(random.randint(8, 10))]
        digits_list = [random.choice(symbols) for i in range(random.randint(2, 4))]
        symbol_list = [random.choice(symbols) for i in range(random.randint(2, 4))]

        password_list = letters_list+ digits_list + symbol_list

        random.shuffle(password_list)

        password = "".join(password_list)
        return password