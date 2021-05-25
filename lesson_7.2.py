class Clothes:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_c(self):
        return self.width / 3.5 + 1.5

    def get_square_s(self):
        return self.height * 1 + 0.5

    @property
    def get_sq_full(self):
        return str(f'Total amount of textile - \n'
                   f' {(self.width / 3.5 + 1.5) + (self.height * 1 + 0.5)}')


class Coat(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 3.5 + 1.5)

    def __str__(self):
        return f'Needed for coat {self.square_c}'


class Suit(Clothes):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_s = round(self.height * 1 + 0.5)

    def __str__(self):
        return f'Needed for suit {self.square_s}'


coat = Coat(2, 4)
suit = Suit(1, 2)
print(coat)
print(suit)
print(coat.get_sq_full)
print(suit.get_sq_full)
print(suit.get_square_c())
print(suit.get_square_s())
