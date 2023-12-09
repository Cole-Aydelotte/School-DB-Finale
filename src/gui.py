import tkinter as tk

class Gui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Sample GUI with Search Bar and Cart')
        self.geometry('800x600')

        self.search_bar = tk.Entry(self)
        self.search_bar.pack()

        search_button = tk.Button(self, text='Search', command=self.search_clicked)
        search_button.pack()

        self.cart_icon = tk.Label(self, text='Cart')
        self.cart_icon.pack()

    def search_clicked(self):
        query = self.search_bar.get()
        return query
