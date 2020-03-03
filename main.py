from tkinter import *
from random import *

upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
lower = "qwertyuiopasdfghjklzxcvbnm"
numbers = "1234567890"
symbols = "#$%&\()*+<=>?!@{|}~-"


def generate_password(length, digits):
    digits_count = len(digits)
    password = ""

    for i in range(length):
        rand = randint(0, digits_count - 1)
        password += digits[rand]

    return password


def calculate_brute_force_time(password, available_digits):
    time = 1

    for i in range(len(password)):
        n = available_digits.index(password[i], 0, len(available_digits)) + 1
        time *= n

    try:
        days = time / (1 * 60 * 60 * 24 * 10000000)
        days = round(days, 2)
    except OverflowError:
        return "<cлишком много>"

    return days


def generate():
    available_digits = ""

    if enable_lower.get() == 1:
        available_digits += lower
    if enable_upper.get() == 1:
        available_digits += upper
    if enable_numbers.get() == 1:
        available_digits += numbers
    if enable_symbols.get() == 1:
        available_digits += symbols

    if available_digits == "":
        return

    length = int(spinbox.get())

    password = generate_password(length, available_digits)

    password_variable.set(password)

    days = calculate_brute_force_time(password, available_digits)

    text = "Если компьютер тратит одну секунду на проверку 10,000,000 паролей, то ваш пароль нужно будет подбирать {0} дн.".format(days)

    textbox.delete("1.0", END)
    textbox.insert(END, text)


tk = Tk()
tk.title("Генератор паролей")

enable_upper = IntVar()
enable_lower = IntVar()
enable_numbers = IntVar()
enable_symbols = IntVar()

password_variable = StringVar()

generate_button = Button(tk, text="Сгенерировать!", command=generate)
generate_button.grid(column=1, row=0)

upper_checkbox = Checkbutton(text="Большие Буквы (QWERTY)", var=enable_upper)
lower_checkbox = Checkbutton(text="Маленькие Буквы (qwerty)", var=enable_lower)
numbers_checkbox = Checkbutton(text="Цифры (12345)", var=enable_numbers)
symbols_checkbox = Checkbutton(text="Спец. Символы (#$%&@)", var=enable_symbols)

upper_checkbox.grid(column=1, sticky=W)
lower_checkbox.grid(column=1, sticky=W)
numbers_checkbox.grid(column=1, sticky=W)
symbols_checkbox.grid(column=1, sticky=W)

entry = Entry(text="Вы ещё не сгенерировали пароль", textvariable=password_variable)
entry.grid(column=2, row=0)

spinbox = Spinbox(from_=1, to=50)
spinbox.grid(column=3, row=0)

textbox = Text(height=10, width=55)
textbox.grid(column=2, row=1, columnspan=2, rowspan=4)

if __name__ == "__main__":
    tk.mainloop()
