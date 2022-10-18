from Category import Category
from Product import Product
from Meny import Meny
produc1 = Product('meet', 12)
produc2 = Product('fish', 32)
produc3 = Product('chees cacke', 22)
produc4 = Product('tiramisu', 18)
arr_of_prosucts1 = [produc1, produc2]
arr_of_prosucts2 = [produc3, produc4]

category1 = Category(arr_of_prosucts1, 'salted')
category2 = Category(arr_of_prosucts2, 'shugared')

meny = Meny([category1, category2])

print(meny.process())


