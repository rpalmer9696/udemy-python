from WidgetCreator import WidgetCreator
from tkinter import StringVar, END


class WidgetContainer:
    def __init__(self, window):
        self.widget_creator = WidgetCreator(window)
        self.title_value = StringVar()
        self.author_value = StringVar()
        self.year_value = StringVar()
        self.isbn_value = StringVar()
        self.widgets = self.init_widgets()

    def get_widgets(self):
        return self.widgets

    def init_widgets(self):
        return {
            "title": self.init_title_widgets(),
            "author": self.init_author_widgets(),
            "year": self.init_year_widgets(),
            "isbn": self.init_isbn_widgets(),
            "listbox": self.init_book_listbox()
        }

    def init_title_widgets(self):
        return (self.widget_creator.create_label("Title", row=0, column=0),
                self.widget_creator.create_input(self.title_value, row=0, column=1))

    def init_author_widgets(self):
        return (self.widget_creator.create_label("Author", row=0, column=2),
                self.widget_creator.create_input(self.author_value, row=0, column=3))

    def init_year_widgets(self):
        return (self.widget_creator.create_label("Year", row=1, column=0),
                self.widget_creator.create_input(self.year_value, row=1, column=1))

    def init_isbn_widgets(self):
        return (self.widget_creator.create_label("ISBN", row=1, column=2),
                self.widget_creator.create_input(self.isbn_value, row=1, column=3))

    def init_book_listbox(self):
        book_listbox = self.widget_creator.create_listbox(
            height=10, width=35, row=2, column=0, row_span=6, column_span=2)

        book_listbox.bind("<<ListboxSelect>>", self.get_selected_row)

        return book_listbox

    def get_values(self):
        book = self.title_value.get(), self.author_value.get(), self.year_value.get(), self.isbn_value.get()
        return book

    def get_selected_row(self, event):
        book = self.widgets["listbox"].get(self.widgets["listbox"].curselection())
        self.title_value.set(book[1])
        self.author_value.set(book[2])
        self.year_value.set(book[3])
        self.isbn_value.set(book[4])
