class Product:
    """ This class defines a product """
    
    def __init__(self, name, price, tax):
        self.name = name
        self.base_price = price
        self.tax_rate = tax

    def __str__(self):
        return f"Product: {self.name} - {self.base_price:.2f}"

    def total_price(self):
        tax_conversion = self.tax_rate / 100
        tax_total = self.base_price * tax_conversion
        total = self.base_price + tax_total
        return total