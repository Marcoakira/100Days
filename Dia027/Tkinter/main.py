from tkinter import *


window = Tk()

window.title("My GUI program")
window.minsize(width=500, height=300)
# window.padding(10)

# Create a label
my_label = Label(text="Hello World!", font=("Helvetica", 24, "bold"))
# my_label.pack(side="left")
# my_label.grid(row=5, column=5)
my_label.pack()

my_label["text"] = "New Hello World!"
my_label.config(text="New Hello World! 2")


# Create a button
''' modo com função de criar um botão'''


def click_me_buttom():
    content = input_text.get()
    my_label.config(text=content)
    # my_label.config(text="Button was clicked!")
    print("Button was clicked!")

    # my_label.pack()
    # print('button was normal again')
    # my_label.config(text="New Hello World! 2")
    # my_label.pack()


button = Button(text='Click me', command = click_me_buttom)
''' modo simples de criar um botão'''
# button = Button(text="Click Me!", command=lambda: print("Hello World!"))
# button.pack(side="right")
'''############################################################'''
button.pack()

# Entry

input_text = Entry(width=50)
input_text.pack()


window.mainloop()