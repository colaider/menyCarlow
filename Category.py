class Category:
    __name_of_category = ''
    __list_of_products = []
    total_price = 0

    def get_name_of_category(self):
        return self.__name_of_category

    def set_name_of_category(self, name):
        self.__name_of_category = name

    def get_list_of_products(self):
        return self.__list_of_products

    def set_list_of_products(self, lis):
        self.__list_of_products = lis

    def get_total_price(self):
        tot = 0
        for el in self.__list_of_products:
            tot += el.prot_price
        return tot
    def sort_products(self):
        self.__list_of_products.sort(key=lambda x: x.prot_price, reverse=True)
        return self.__list_of_products

    def __init__(self, lis=[], name=''):
        self.__name_of_category = name
        self.__list_of_products = lis
        self.total_price = self.get_total_price()

