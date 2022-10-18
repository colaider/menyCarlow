class Product:
    __name = ''
    __price = 0
    prot_price = 0

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.prot_price = self.get_price()