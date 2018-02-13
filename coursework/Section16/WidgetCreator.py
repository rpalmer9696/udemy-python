from tkinter import *


class WidgetCreator:
    def __init__(self, window):
        self.window = window

    def create_button(self, text, command, row, column, width):
        button = Button(self.window, text=text, command=command, width=width)
        button.grid(row=row, column=column)
        return button

    def create_label(self, text, row, column):
        label = Label(self.window, text=text)
        label.grid(row=row, column=column)
        return label

    def create_input(self, text_variable, row, column):
        entry = Entry(self.window, textvariable=text_variable)
        entry.grid(row=row, column=column)
        return entry

    def create_listbox(self, height, width, row, column, row_span, column_span):
        listbox = Listbox(self.window, height=height, width=width)
        listbox.grid(row=row, column=column, rowspan=row_span, columnspan=column_span)
        return listbox
