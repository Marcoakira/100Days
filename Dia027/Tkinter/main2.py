from tkinter import *

def click_me_buttom():
    content = input_text.get()
    my_label.config(text=content)
    # my_label.config(text="Button was clicked!")
    print("Button was clicked!")

# Create a window
window = Tk()
window.title("My GUI program")
window.minsize(width=500, height=300)
window.config( padx=40, pady=40)

# Create a label
my_label = Label(text="Hello World!", font=("Helvetica", 24, "bold"))
my_label.config(text="New Hello World! 2")
my_label.grid(row=0, column=0)
my_label.config(padx=10, pady=10)
# my_label.place(x=100, y=50)
# my_label["text"] = "New Hello World!"
# my_label.pack()


# Entry
input_text = Entry(width=50)
print(input_text.get())
input_text.grid(row=2, column=4)
# input_text.config(padx=10, pady=10)
# input_text.place(x=100, y=100)
# input_text.pack(side='left')

# Create a button
button = Button(text='Click me', command = click_me_buttom)
button.grid(row=0, column=2)
button.config(padx=10, pady=10)

# Create a new button
button2 = Button(text='new button')
button2.grid(row=1, column=1)
button2.config(padx=10, pady=10)

# button.pack(side='left')
# button.place(x=100, y=150)
''' modo simples de criar um botão'''
# button = Button(text="Click Me!", command=lambda: print("Hello World!"))
# button.pack(side="right")
# button.pack()

# Start the GUI
window.mainloop()