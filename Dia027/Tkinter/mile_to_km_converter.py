from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.geometry('400x200')
window.configure(padx=30, pady=30)

# input
def input_miles():
    content = input_text.get()
    content = float(content)
    os_km = content * 1.60934
    label_input.config(text=os_km)
    # my_label.config(text="Button was clicked!")
    print("Button was clicked!")

# label for mile
label_miles = Label(window, text="Miles", font=("Arial", 16, "bold"))
label_miles.grid(column=2, row=0)

# label for is equal to
label_is = Label(window, text="is equal to", font=("Arial", 16, "bold"))
label_is.grid(column=0, row=1)

# label for input
label_input = Label(window, text="0", font=("Arial", 16, "bold"))
label_input.grid(column=1, row=1)

# label for km
label_km = Label(window, text="Km", font=("Arial", 16, "bold"))
label_km.grid(column=3, row=1)

# input / entry

input_text = Entry(width=5)
print(input_text.get())
input_text.grid(row=0, column=1)

# button

button2 = Button(text='Calculate', command=input_miles)
button2.grid(row=2, column=1)
button2.config(padx=10, pady=10)




window.mainloop()