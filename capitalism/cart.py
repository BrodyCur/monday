from product import Product

class Cart():
    """ this class defines a shopping cart """

    def __init__(self):
        self.product_list = []

    def __str__(self):
        listings = '\n'.join(str(product) for product in self.product_list)

        # temp = []
        # for product in self.product_list:
        #     temp.append(str(product))
        # listings = "\n".join(temp)

        return f"Items in cart:\n{listings}\nTotal before tax: ${self.total_cost_before_tax():.2f}\nTotal after tax: ${self.total_cost_after_tax():.2f}\nMost expensive item: {self.find_most_expensive()}"

    def add_product(self, item):
        self.product_list.append(item)

    def remove_product(self, item):
        self.product_list.remove(item)

    def total_cost_before_tax(self):
        total = 0
        for product in self.product_list:
            total += product.base_price
        return total

    def total_cost_after_tax(self):
        total = 0
        for product in self.product_list:
            total += product.total_price()
        return total

    def find_most_expensive(self):
        pass

apple = Product('apple', 14.65, 15)
orange = Product('orange', 3.99, 15)
meat = Product('Tenderloin', 10.99, 15)

my_cart = Cart()

my_cart.add_product(apple)
my_cart.add_product(orange)
my_cart.add_product(meat)

print(my_cart)

my_cart.remove_product(orange)

print(my_cart)