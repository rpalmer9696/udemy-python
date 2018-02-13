from tkinter import *
from WidgetCreator import WidgetCreator
from Book import Book


def get_values():
    book = title_value.get(), author_value.get(), year_value.get(), isbn_value.get()
    refresh()
    return book


def get_selected_row(event):
    book = book_listbox.get(book_listbox.curselection())
    title_value.set(book[1])
    author_value.set(book[2])
    year_value.set(book[3])
    isbn_value.set(book[4])


def show_data():
    book_listbox.delete(0, END)
    for book in bookDao.fetch():
        book_listbox.insert(END, book)


def search_data():
    book_listbox.delete(0, END)
    for book in bookDao.get(get_values()):
        book_listbox.insert(END, book)


def add_book():
    bookDao.add(get_values())
    show_data()


def update_data():
    book = book_listbox.get(book_listbox.curselection())
    bookDao.update(book[0], get_values())
    show_data()


def delete_book():
    book = book_listbox.get(book_listbox.curselection())
    bookDao.delete(book[0])
    show_data()


def refresh():
    title_input.delete(0, END)
    author_input.delete(0, END)
    year_input.delete(0, END)
    isbn_input.delete(0, END)


window = Tk()
bookDao = Book()
widgetCreator = WidgetCreator(window)

title_label = widgetCreator.create_label("Title", row=0, column=0)
title_value = StringVar()
title_input = widgetCreator.create_input(title_value, row=0, column=1)

author_label = widgetCreator.create_label("Author", row=0, column=2)
author_value = StringVar()
author_input = widgetCreator.create_input(author_value, row=0, column=3)

year_label = widgetCreator.create_label("Year", row=1, column=0)
year_value = StringVar()
year_input = widgetCreator.create_input(year_value, row=1, column=1)

isbn_label = widgetCreator.create_label("ISBN", row=1, column=2)
isbn_value = StringVar()
isbn_input = widgetCreator.create_input(isbn_value, row=1, column=3)

book_listbox = widgetCreator.create_listbox(height=10, width=35, row=2, column=0, row_span=6, column_span=2)
book_scrollbar = Scrollbar(window)
book_scrollbar.grid(row=2, column=2, rowspan=6)

book_listbox.configure(yscrollcommand=book_scrollbar.set)
book_scrollbar.configure(command=book_listbox.yview)

book_listbox.bind("<<ListboxSelect>>", get_selected_row)


view_all_button = widgetCreator.create_button("View all", width=12, row=2, column=3, command=show_data)
search_button = widgetCreator.create_button("Search entry", width=12, row=3, column=3, command=search_data)
add_button = widgetCreator.create_button("Add entry", width=12, row=4, column=3, command=add_book)
update_button = widgetCreator.create_button("Update", width=12, row=5, column=3, command=update_data)
delete_button = widgetCreator.create_button("Delete", width=12, row=6, column=3, command=delete_book)
clear_button = widgetCreator.create_button("Clear", width=12, row=7, column=3, command=refresh)

show_data()
window.mainloop()
