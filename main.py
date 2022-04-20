from tkinter import *


def calc():
    km_output['text'] = round(float(miles_input.get()) * 1.6093)


window = Tk()
window.minsize(width=300, height=150)
window.title('Mile to Km Converter')
window.config(padx=20, pady=20)


equal_lable = Label(text='Is equal to: ')
equal_lable.config(padx=10, pady=10)
equal_lable.grid(column=0, row=1)

miles_input = Entry(width=10)
equal_lable.config(padx=10, pady=10)
miles_input.grid(column=1, row=0)

km_output = Label(width=10, text=0)
equal_lable.config(padx=10, pady=10)
km_output.grid(column=1, row=1)

miles_lable = Label(text='Miles')
equal_lable.config(padx=10, pady=10)
miles_lable.grid(column=2, row=0)

km_lable = Label(text='Km')
equal_lable.config(padx=10, pady=10)
km_lable.grid(column=2, row=1)

calc_button = Button(text='Calculate', command=calc, width=7)
equal_lable.config(padx=10, pady=10)
calc_button.grid(column=1, row=2)


window.mainloop()

