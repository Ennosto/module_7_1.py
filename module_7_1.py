class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self, file_name='products.txt'):
        self.__file_name = file_name

    def get_products(self):
        file_read = open(self.__file_name, 'r')
        list_ = file_read.read()
        file_read.close()
        return list_

    def add(self, *products):
        file_add = open(self.__file_name, 'r+')
        for i in products:
            if i.name not in self.get_products():
                file_add.write(f'{i}\n')
            else:
                print(f'Продукт {i} уже есть в магазине')
        file_add.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
