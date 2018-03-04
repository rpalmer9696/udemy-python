from ButtonHandlers import ButtonHandlers
from DataAccessObject.Book import Book as BookDAO
from tkinter import Tk
from WidgetContainer import WidgetContainer
from WidgetCreator import WidgetCreator


class Main:
    def __init__(self, book_dao):
        self.window = Tk()
        self.widget_creator = WidgetCreator(self.window)
        self.widget_container = WidgetContainer(self.window)
        self.button_handlers = ButtonHandlers(book_dao, self.widget_container, self.widget_creator)

    def main_loop(self):
        self.button_handlers.show_books()
        self.window.mainloop()


with BookDAO() as bookDao:
    main = Main(bookDao)
    main.main_loop()

