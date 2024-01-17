from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609, 2)
    kilometer_result_label.config(text=f"{km}")

# for window
window = Tk()
window.title("Mile to KM Converter")
# window.minsize(width=20, height=20)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

label_miles = Label(text="Miles")

label_equal = Label(text="is equal to")

label_km = Label(text="Km")

kilometer_result_label = Label(text="0")

label_miles.grid(column=2, row=0)
label_equal.grid(column=0, row=1)
label_km.grid(column=2, row=1)
kilometer_result_label.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)

calculate_button.grid(column=1, row=3)

window.mainloop()
