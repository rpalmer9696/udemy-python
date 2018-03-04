from tkinter import *


def convert_to_measurements():
    clear_text()

    try:
        grams = float(kg_value.get()) * 1000
        pounds = float(kg_value.get()) * 2.20462
        ounces = float(kg_value.get()) * 35.274

        gram_text.insert(END, grams)
        pounds_text.insert(END, pounds)
        ounces_text.insert(END, ounces)
    except ValueError:
        gram_text.insert(END, "NaN")
        pounds_text.insert(END, "NaN")
        ounces_text.insert(END, "NaN")


def clear_text():
    gram_text.delete(1.0, END)
    pounds_text.delete(1.0, END)
    ounces_text.delete(1.0, END)


window = Tk()

kg_label = Label(window, text="Kg")
kg_label.grid(row=0, column=0)

kg_value = StringVar()
kg_input = Entry(window, textvariable=kg_value)
kg_input.grid(row=0, column=1)

convert_button = Button(window, text="Convert", command=convert_to_measurements)
convert_button.grid(row=0, column=2)

gram_text = Text(window, height=1, width=20)
gram_text.grid(row=1, column=0)

pounds_text = Text(window, height=1, width=20)
pounds_text.grid(row=1, column=1)

ounces_text = Text(window, height=1, width=20)
ounces_text.grid(row=1, column=2)

window.mainloop()
