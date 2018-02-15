from Model.Book import Book as BookModel
from tkinter import END


class ButtonHandlers:
    def __init__(self, book_dao, widget_container, widget_creator):
        self.book = BookModel(book_dao)
        self.widget_container = widget_container
        self.widget_creator = widget_creator

        self.init_buttons()

    def show_books(self):
        self.widget_container.get_widgets()["listbox"].delete(0, END)
        for book in self.book.show_books():
            self.widget_container.get_widgets()["listbox"].insert(END, book)
        self.refresh()

    def search_book(self, book):
        self.widget_container.get_widgets()["listbox"].delete(0, END)
        for book in self.book.search_book(book):
            self.widget_container.get_widgets()["listbox"].insert(END, book)

    def add_book(self, book):
        self.book.add_book(book)
        self.show_books()
        self.refresh()

    def update_book(self, book):
        current_book = self.widget_container.get_widgets()["listbox"].get(self.widget_container.get_widgets()["listbox"].curselection())
        self.book.update_book(current_book[0], book)
        self.show_books()
        self.refresh()

    def delete_book(self):
        book = self.widget_container.get_widgets()["listbox"].get(self.widget_container.get_widgets()["listbox"].curselection())
        self.book.delete_book(book[0])
        self.show_books()
        self.refresh()

    def refresh(self):
        self.widget_container.get_widgets()["title"][1].delete(0, END)
        self.widget_container.get_widgets()["author"][1].delete(0, END)
        self.widget_container.get_widgets()["year"][1].delete(0, END)
        self.widget_container.get_widgets()["isbn"][1].delete(0, END)

    def init_buttons(self):
        self.widget_creator.create_button(
            "View all", width=12, row=2, column=3, command=lambda: self.show_books())
        self.widget_creator.create_button(
            "Search entry", width=12, row=3, column=3, command=lambda: self.search_book(self.widget_container.get_values()))
        self.widget_creator.create_button(
            "Add entry", width=12, row=4, column=3, command=lambda:  self.add_book(self.widget_container.get_values()))
        self.widget_creator.create_button(
            "Update", width=12, row=5, column=3, command=lambda: self.update_book(self.widget_container.get_values()))
        self.widget_creator.create_button(
            "Delete", width=12, row=6, column=3, command=lambda: self.delete_book())
        self.widget_creator.create_button(
            "Clear", width=12, row=7, column=3, command=self.refresh)
