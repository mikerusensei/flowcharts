class Product:
    def __init__(self, name, price, expiration) -> None:
        self.name = name
        self.price = price
        self.expiration = expiration

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Expiration: {self.expiration}"