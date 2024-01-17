from tkinter import *;


def km_to_miles():
    km = float(Km_input.get())
    miles = round(km / 1.609, 2)
    miles_result_label.config(text=f"{miles}")


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

# text on screen
label_KM = Label(text="Km")
label_KM.grid(row=0, column=2)
label_equals = Label(text="is equal to")
label_equals.grid(column=0, row=1)
label_miles = Label(text="Miles")
label_miles.grid(row=1, column=2)
miles_result_label = Label(text="0")
miles_result_label.grid(row=1, column=1)


# Entry
Km_input = Entry(width=10)
Km_input.grid(column=1, row=0)
calculate_button = Button(text="Calculate", command=km_to_miles)
calculate_button.grid(column=1, row=3)
window.mainloop()



