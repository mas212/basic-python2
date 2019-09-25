class Cars:
    def __init__(self, name, merk, price):
        self.name = name
        self.merk = merk
        self.price = price

    def getPrice(self):
        return f'{price}'

items = Cars('scopy', 'honda', 20.0000)

print(items)
print(items.getPrice())
