#  Override the methods on your Money class so that you can perform numeric operations between two instances of the money class
# Implement >= > <= < + - == != * operator overloads
# Implement the conversion rates for USD, JPY, EUR, and BTC


class Money:

    def __init__(self, value, currency):
        self.value = value
        self.currency = currency
#  create a money class that can store amount and currency symbol

    def convert_to_usd(self):
        if self.currency == "USD":
            return self.value / 1.00
        elif self.currency == "EUR":
            return self.value / .89
        elif self.currency == "JPY":
            return self.value / 100.3
        elif self.currency == "BTC":
            return self.value / .006

    def __add__(self, other):
        left = self.convert_to_usd()
        right = other.convert_to_usd()
        return left + right

    def __mul__(self, other):
        left = self.convert_to_usd()
        right = other.convert_to_usd()
        return left * right

    def __str__(self):
        return str(self.value)

    def __ge__(self, other):
        left = self.convert_to_usd()
        right = other.convert_to_usd()
        return left >= right

    def __gt__(self, other):
        left = self.convert_to_usd()
        right = other.convert_to_usd()
        return left > right

    def __le__(self, other):
        left = self.convert_to_usd()
        right = other.convert_to_usd()
        return left <= right

    def __lt__(self, other):
        left = self.convert_to_usd()
        right = other.convert_to_usd()
        return left < right

    def __sub__(self, other):
        left = self.convert_to_usd()
        right = other.convert_to_usd()
        return left - right

    def __eq__(self, other):
        left = self.convert_to_usd()
        right = other.convert_to_usd()
        return left == right

    def __ne__(self, other):
        left = self.convert_to_usd()
        right = other.convert_to_usd()
        return left != right

usd = Money(5, "USD")
print(usd.convert_to_usd())
eur = Money(5, "EUR")
print(eur.convert_to_usd())
jpy = Money(5000, "JPY")
print(jpy.convert_to_usd())
btc = Money(5, "BTC")
print(btc.convert_to_usd())

print(usd != jpy)

# money("USD", 23.0) > money("EUR", 15.0)
# True
