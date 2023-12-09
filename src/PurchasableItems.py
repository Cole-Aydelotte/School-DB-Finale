'''
Created By: <Cole Aydelotte>
'''
import random

class PurchasableItems:
    def __init__(self, item_list=None):
        self.Items = item_list if item_list is not None else []

    def create_item(self, stock, price, name):
        barcode = self.get_barcode()
        while any(barcode == item.get_barcode() for item in self.Items):
            barcode = self.get_barcode()

        item = Purchasable(stock, barcode, price, name)  # Assuming Purchasable class exists
        self.Items.append(item)

    def get_barcode(self):
        rand_num = random.randint(1000, 9999)
        return str(rand_num)

    def get_items(self):
        return self.Items

    def __str__(self):
        result = ""
        for idx, item in enumerate(self.Items):
            if idx == 0:
                result += f"Stock: {item.get_stock()} Barcode: {item.get_barcode()} Price: {item.get_price()} Name: {item.get_name()} "
            else:
                result += f", Stock: {item.get_stock()} Barcode: {item.get_barcode()} Price: {item.get_price()} Name: {item.get_name()} "
        return result

#New Class

class ShoppingCart:
    def __init__(self, the_list=None):
        self.items = the_list if the_list is not None else []

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items

#New Class

class Purchasable:
    def __init__(self, stock, barcode, price, name):
        self.stock = stock
        self.barcode = barcode
        self.price = price
        self.name = name
    
    def get_price(self):
        return self.price
    
    def get_barcode(self):
        return self.barcode
    
    def get_name(self):
        return self.name
    
    def get_stock(self):
        return self.stock
    
    def set_stock(self, stock):
        self.stock = stock

#New Class

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def get_quantity(self):
        return self.quantity
    
    def set_quantity(self, quantity):
        self.quantity = quantity
