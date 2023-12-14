import tkinter as tk
from tkinter import messagebox

from email_receipt import send_email


'''
Creates a gui that is very simple with a required input of a 
email on the right side of the screen, once submitted you can 
search for car parts and all items conatining the query will 
show up with a add to cart button. once done filling cart you 
click the purchase button and a email containing the 
transaction id, total price, and items will be sent to the email provided.
'''
class Gui(tk.Tk):
    def __init__(self, cursor):
        super().__init__()
        self.cursor = cursor
        self.shopping_cart = shopping_cart()
        self.email_commited = False
        self.title('Car Parts')
        self.geometry('800x600')
        self.configure(bg='black')

        self.search_bar = tk.Entry(self, bg='white')
        self.search_bar.pack()

        search_button = tk.Button(self, text='Search', command=self.search_clicked)
        search_button.pack()

        self.cart_icon = tk.Label(self, bg='black', text='Cart', fg='white')
        self.cart_icon.place(x=400, y= 300)

        self.canvas = tk.Canvas(self, bg='white')
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.results_frame = tk.Frame(self.canvas, bg='white')
        self.canvas.create_window((0, 0), window=self.results_frame, anchor=tk.NW)

        self.cart_contents_label = tk.Label(self, text='Cart', bg='white')
        self.cart_contents_label.pack()

        self.cart_contents_frame = tk.Frame(self.canvas, bg='white')
        self.canvas.create_window((0, 0), window=self.cart_contents_frame, anchor=tk.NW)

        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.email_button = tk.Button(self, text='Submit', command=self.email_user)
        self.email_button.pack()

        purchase_submit = tk.Button(self, bg='white', text=f'Purchase', command=self.purchase_items)
        purchase_submit.pack(side=tk.BOTTOM, anchor=tk.SE)

    def search_query(self, query):
        sql_query = f'SELECT item_name, item_id FROM items WHERE item_name LIKE "%{query}%";'
        self.cursor.execute(sql_query)
        results = self.cursor.fetchall()
        for line in results:
            result_label = tk.Label(self.results_frame, text=line[0], bg='white')
            result_label.pack()
            purchase_button = tk.Button(self.results_frame, text='Add to cart', command=lambda item_name=line[0], item_id=line[1]: self.purchase_item(item_name, item_id))
            purchase_button.pack()

        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

    def search_clicked(self):
        if self.email_commited == True:
            query = self.search_bar.get()
            self.clear_results()
            self.search_query(query)
        else:
            messagebox.showinfo("Alert", "Must Enter Email before continuing.")

    def clear_results(self):
        self.results_frame.destroy()
        self.results_frame = tk.Frame(self.canvas, bg='white')
        self.canvas.create_window((0, 0), window=self.results_frame, anchor=tk.NW)

    def purchase_item(self, item_name, item_id):
        self.shopping_cart.add_item(item_name, item_id)
        self.update_cart_display()

    def email_user(self):
        self.email = self.email_entry.get()
        self.email_commited = True
        self.email_entry.pack_forget()
        self.email_button.pack_forget()
        self.update_cart_display()

    def update_cart_display(self):
        self.cart_items = [item[0] for item in self.shopping_cart.items]
        self.cart_contents_label.config(text='\n'.join(self.cart_items))
        
        for item_name, item_id in self.shopping_cart.get_Items():
            purchase_button = tk.Button(self.cart_contents_frame, bg='white', text=f'Purchase {item_name}')
            purchase_button.pack(side=tk.TOP, anchor=tk.NE)

    def purchase_items(self):
        lst = self.shopping_cart.get_Items()
        for name, it_id in lst:
            self.cursor.execute(f"UPDATE items SET item_quantity = item_quantity - 1 WHERE item_name = '{name}';")
            self.cursor.execute("commit;")
        send_email(self.email, lst, self.cursor)
        self.quit

class shopping_cart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, item_id):
        item_creds = item_name, item_id
        self.items.append(item_creds)
    
    def get_Items(self):
        return self.items
    