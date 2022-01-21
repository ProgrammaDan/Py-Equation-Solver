from tkinter import *


def analyze(userInput: str, xValue: float):
    def num_read(string: str, start: int, end: int):
        i = 0
        positive = 0
        decimals = 0
        decimalPlace = 0
        counter = 0
        for element in string[start:end]:
            if element == "-":
                positive += 1
                counter += 1
            elif element == "1":
                if decimals == 1:
                    i = i + (1 * (10 ** decimalPlace))
                    decimalPlace -= 1
                    counter += 1
                else:
                    i = (i * 10) + 1
                    counter += 1
            elif element == "2":
                if decimals == 1:
                    i = i + (2 * (10 ** decimalPlace))
                    decimalPlace -= 1
                    counter += 1
                else:
                    i = (i * 10) + 2
                    counter += 1
            elif element == "3":
                if decimals == 1:
                    i = i + (3 * (10 ** decimalPlace))
                    decimalPlace -= 1
                    counter += 1
                else:
                    i = (i * 10) + 3
                    counter += 1
            elif element == "4":
                if decimals == 1:
                    i = i + (4 * (10 ** decimalPlace))
                    decimalPlace -= 1
                    counter += 1
                else:
                    i = (i * 10) + 4
                    counter += 1
            elif element == "5":
                if decimals == 1:
                    i = i + (5 * (10 ** decimalPlace))
                    decimalPlace -= 1
                    counter += 1
                else:
                    i = (i * 10) + 5
                    counter += 1
            elif element == "6":
                if decimals == 1:
                    i = i + (6 * (10 ** decimalPlace))
                    decimalPlace -= 1
                    counter += 1
                else:
                    counter += 1
                    i = (i * 10) + 6
            elif element == "7":
                if decimals == 1:
                    i = i + (7 * (10 ** decimalPlace))
                    decimalPlace -= 1
                    counter += 1
                else:
                    i = (i * 10) + 7
                    counter += 1
            elif element == "8":
                if decimals == 1:
                    i = i + (8 * (10 ** decimalPlace))
                    decimalPlace -= 1
                    counter += 1
                else:
                    i = (i * 10) + 8
                    counter += 1
            elif element == "9":
                if decimals == 1:
                    i = i + (9 * (10 ** decimalPlace))
                    decimalPlace -= 1
                    counter += 1
                else:
                    i = (i * 10) + 9
                    counter += 1
            elif element == "0":
                if decimalPlace == 0:
                    i = i * 10
                    counter += 1
                elif decimalPlace < 0:
                    decimalPlace -= 1
                    counter += 1
            elif element == ".":
                decimals += 1
                decimalPlace -= 1
                counter += 1
                if decimals > 1:
                    print("Error: more than one decimal point in one number")
                    break
                else:
                    pass
            elif element == " ":
                pass
            elif counter > 0:
                break
        if positive % 2 == 1:
            i = i * -1
        if counter == 0:
            return None
        else:
            return i

    def solve(a, b, c, x):
        return a * (x ** 2) + b * x + c

    def clean(equation):
        result = equation.replace(' ', '')
        result = result.replace('-x', '-1x')
        return result

    def find_x2(equation):
        for x in range(0, len(equation)):
            if equation[x:x + 3] == 'x^2':
                return x + 2
        return -1

    def find_x(equation):
        for x in range((find_x2(equation) + 1), len(equation)):
            if equation[x] == 'x':
                return x
        return -1

    equation = clean(userInput)
    x = xValue

    a = 1
    b = 1
    c = 0
    #    print(f'x^2 location: {find_x2(equation)}')
    #    print(f'x location:   {find_x(equation)}')

    #   get value of a
    if find_x2(equation) != -1 and num_read(equation, 0, find_x2(equation)) is not None:
        a = num_read(equation, 0, find_x2(equation))
    elif find_x2(equation) == -1:
        a = 0
    else:
        pass

    #   get value of b
    if find_x(equation) != -1 and num_read(equation, find_x2(equation) + 1, find_x(equation)) is not None:

        b = num_read(equation, find_x2(equation) + 1, find_x(equation))
    elif find_x(equation) == -1:
        b = 0
    else:
        pass

    #   get value of c
    if find_x2(equation) + 1 == len(equation) or find_x(equation) + 1 == len(equation):
        pass
    elif find_x(equation) == -1 and find_x2(equation) != -1:
        c = num_read(equation, find_x2(equation) + 1, len(equation))
    elif num_read(equation, find_x(equation) + 1, len(equation)) is not None:
        c = num_read(equation, find_x(equation) + 1, len(equation))

    #    print(a, b, c)
    #    print(f'Y = {solve(a,b,c,x)}')
    return solve(a, b, c, x)


# create root
root = Tk()
root.title('Equation Solver')
root.geometry('600x400')


# create functions
def button_command():
    result.config(text=entry1.get())
    return None


def keyboard_get_answer(e):
    if len(entry1.get()) > 0 and len(entry2.get()) > 0:
        try:
            result.config(text=analyze(entry1.get(), float(entry2.get())))
            y_equals.config(text='f(' + entry2.get() + ') = ')
        except ValueError:
            pass
    return None

def button_get_answer():
    if len(entry1.get()) > 0 and len(entry2.get()) > 0:
        try:
            result.config(text=analyze(entry1.get(), float(entry2.get())))
            y_equals.config(text='f(' + entry2.get() + ') = ')
        except ValueError:
            pass
    return None

def clear_all():
    if len(entry1.get()) > 0:
        entry1.delete(0, END)
    if len(entry2.get()) > 0:
        entry2.delete(0, END)
    result.config(text='')
    y_equals.config(text="f( ) = ")
    return None


# create buttons
enter_button = Button(root, text='calculate', width=50, command=button_get_answer)
enter_button.place(relx=.19, rely=.9)

exit_button = Button(root, text='exit', width=7, command=root.destroy)
exit_button.place(relx=.875, rely=.9)

clear_button = Button(root, text='clear all', command=clear_all)
clear_button.place(relx=.025, rely=.9)

# create entry boxes
entry1 = Entry(root, width=20)
entry1.place(relx=.5, rely=.2, anchor='center')

entry2 = Entry(root, width=20, )
entry2.place(relx=.5, rely=.285, anchor='center')

# create labels
instructions = Label(root, text='Enter any quadratic or linear equation')
instructions.place(relx=.5, rely=.12, anchor='center')

function = Label(root, text='f(x) = ')
function.place(relx=.4, rely=.195, anchor='e')

solve_for = Label(root, text='Solve for: ')
solve_for.place(relx=.4, rely=.285, anchor='e')

y_equals = Label(root, text='f( ) = ')
y_equals.place(relx=.4, rely=.3725, anchor='e')

result = Label(root, text='')
result.place(relx=.395, rely=.373, anchor='w')

# add ability to react to keyboard 'enter'
root.bind('<Return>', keyboard_get_answer)

root.mainloop()
