from tkinter import *
from random import *


def clicked():
    alpha = "qwertyuioplkjhgfdsazxcvbnm"
    numbers = "0123456789"
    symbols = "!@_/&"
    password = ""
    length_of_password = int(length.get())
    if int(user_choice.get()) == 1:
        result.delete(0, END)
        first_option = alpha + alpha.upper()
        for i in range(length_of_password):
            p = choice(first_option)
            password += p
        result.insert(0, password)
    elif int(user_choice.get()) == 2:
        result.delete(0, END)
        second_option = numbers
        for i in range(length_of_password):
            p = choice(second_option)
            password += p
        result.insert(0, password)
    elif int(user_choice.get()) == 3:
        result.delete(0, END)
        third_option = alpha + alpha.upper() + numbers
        for i in range(length_of_password):
            p = choice(third_option)
            password += p
        result.insert(0, password)
    elif int(user_choice.get()) == 4:
        result.delete(0, END)
        fourth_option = alpha + alpha.upper() + numbers + symbols
        for i in range(length_of_password):
            p = choice(fourth_option)
            password += p
        result.insert(0, password)
    else:
        result.delete(0, END)
        result.insert(0, "ERROR")


root = Tk()
root.title("Password Generator")
root.geometry("550x490")
root.configure(bg="#99AFE0")

header = Label(root, text="Password Generator", font=("Arial", 15), bg="#AB9CF7")
header.place(relx=0.32, rely=0.02)

lbl1 = Label(root, font=("Arial", 11), bg="#AB9CF7", text="Enter:\n"
                                                          "1 to get password which consists of only letters\n"
                                                          "2 to get password which consists of only numbers\n"
                                                          "3 to get password which consists of numbers and letters\n"
                                                          "4 to get password which consists of numbers,letters and "
                                                          "symbols")
lbl1.place(relx=0.05, rely=0.13, relwidth=0.9)

option = Label(root, text="Enter your choice :", font=("Arial", 11), bg="#AB9CF7")
option.place(relx=0.1, rely=0.4)

user_choice = Entry()
user_choice.place(relx=0.1, rely=0.48, relheight=0.05)

length_password = Label(root, text="Enter the length of password :", font=("Arial", 11), bg="#AB9CF7")
length_password.place(relx=0.5, rely=0.4, relwidth=0.4)

length = Entry()
length.place(relx=0.55, rely=0.48, relwidth=0.3, relheight=0.05)

btn = Button(root, text="Get password", bg="#DB1B18", fg="#FFFFFF", width=13, command=clicked, font=("Arial", 11))
btn.place(relx=0.33, rely=0.62, relwidth=0.3)

result = Entry()
result.place(relx=0.33, rely=0.7, relwidth=0.3, relheight=0.05)

root.mainloop()
