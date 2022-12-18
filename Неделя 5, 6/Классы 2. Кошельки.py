class BaseWallet:
    exchange_rate = 1

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def to_base(self):
        return (self.amount * self.exchange_rate)

    def spend_all(self):
        if self.amount >= 0:
            self.amount = 0

    def __add__(self, other):
        if isinstance(other, BaseWallet):
            new_amount = (self.amount + other.amount * (other.exchange_rate / self.exchange_rate))
        else:
            new_amount = self.amount + int(other)
        return self.__class__(self.name, new_amount)

    def __sub__(self, other):
        if isinstance(other, BaseWallet):
            new_amount = (self.amount - other.amount * (other.exchange_rate / self.exchange_rate))
        else:
            new_amount = self.amount - int(other)
        return self.__class__(self.name, new_amount)

    def __rsub__(self, other):
        if isinstance(other, BaseWallet):
            new_amount = (other.amount * (other.exchange_rate / self.exchange_rate) - self.amount)
        else:
            new_amount = int(other) - self.amount
        return self.__class__(self.name, new_amount)

    def __mul__(self, other):
        if isinstance(other, BaseWallet):
            new_amount = (self.amount * (other.amount * (other.exchange_rate / self.exchange_rate)))
        else:
            new_amount = self.amount * int(other)
        return self.__class__(self.name, new_amount)

    def __truediv__(self, other):
        if isinstance(other, BaseWallet):
            new_amount = (self.amount / (other.amount * (other.exchange_rate / self.exchange_rate)))
        else:
            new_amount = self.amount / int(other)
        return self.__class__(self.name, new_amount)

    def __rtruediv__(self, other):
        if isinstance(other, BaseWallet):
            new_amount = ((other.amount * (other.exchange_rate / self.exchange_rate)) / self.amount)
        else:
            new_amount = int(other) / self.amount
        return self.__class__(self.name, new_amount)

    def __eq__(self, other):
        return (self.amount == other.amount) and (self.__class__ == other.__class__)

    __radd__, __iadd__ = __add__, __add__

    __isub__ = __sub__

    __rmul__, __imul__ = __mul__, __mul__

    __idiv__ = __truediv__

    def __str__(self):
        return f'{self.__class__.__name__} {self.name} {self.amount}'


class RubbleWallet(BaseWallet):
    exchange_rate = 1

    def __str__(self):
        return f'Rubble Wallet {self.name} {self.amount}'


class DollarWallet(BaseWallet):
    exchange_rate = 60

    def __str__(self):
        return f'Dollar Wallet {self.name} {self.amount}'


class EuroWallet(BaseWallet):
    exchange_rate = 70

    def __str__(self):
        return f'Euro Wallet {self.name} {self.amount}'

if __name__ == "__main__":
    pass