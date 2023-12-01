'''
Created By: <Cole Aydelotte>
'''
class Purchase:
    def __init__(self, pass_cart, purchasable_items, phone_number):
        self.cart = pass_cart
        self.purr_list = purchasable_items
        self.receipt = Receipt(phone_number)

        for cart_item in self.cart.get_items():
            for purr_item in self.purr_list:
                if cart_item.get_name() == purr_item.get_name():
                    new_stock = purr_item.get_stock() - cart_item.get_quantity()
                    purr_item.set_stock(new_stock)
                    self.receipt.add_item(purr_item)

        self.receipt.send_receipt()

#New Class

class Receipt:
    def __init__(self, pn):
        self.items = []
        self.phone_number = pn

    def send_receipt(self):
        pass 

    def add_item(self, item):
        self.items.append(item)
