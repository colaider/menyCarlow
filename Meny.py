from operator import attrgetter
class Meny:
    __arr_of_categories = []
    __arr_of_choosen = {}

    def append_arr_of_choosen(self, key, value):
        self.__arr_of_choosen[key] = value

    def get_arr_of_af_categories(self):
        return self.__arr_of_categories

    def set_arr_of_categories(self, arr):
        self.__arr_of_categories = arr

    def sort_list_of_categories(self):
        self.__arr_of_categories.sort(key=lambda x: x.total_price, reverse=True)
        return self.__arr_of_categories

    def process(self):
        inpu = str(input('type start to see the list of categories: '))
        if inpu == 'start':
            for el in self.__arr_of_categories:
                print(el.get_name_of_category(), 'total price', el.total_price)

            inpu = str(input('\ntype the name of category: '))
            for el in self.__arr_of_categories:
                if el.get_name_of_category() == inpu:
                    print('list of products and prices in', el.get_name_of_category(), '\n')
                    for elements in el.get_list_of_products():
                        print(elements.get_name(), '-->', elements.get_price())
                    inpu = str(input('choose name of product'))
                    for elements in el.get_list_of_products():
                        if inpu == elements.get_name():
                            self.append_arr_of_choosen(el.get_name_of_category(), elements)
                    inpu = str(input('\ndo you want something else press yes to start again: '))
                    if inpu == 'yes':
                        self.process()
                    elif inpu == 'no':
                        return self.__arr_of_choosen
        else:
            inpu = str(input('\nyou put something wrong put again or stop: '))
            if inpu == 'again':
                 self.process()
            else:
                return

    def __init__(self, arr):
        self.__arr_of_categories = arr