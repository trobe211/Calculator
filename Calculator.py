from tkinter import *

# Creating the main window
main_window = Tk()
main_window.title('Calculator')
main_window.configure(background='white')

# Defining the functions
# Adds the value of the button to the current operation
def add(num):
    display_window['text'] = str(display_window['text']) + str(num)

# Evaluates the current expression in the window
# Uses a try and except to display a general error message
def answer():
    try:
        display_window['text'] = round(eval(display_window['text']),5)
    except:
        display_window['text'] = 'ERROR'

# Clears anything in the display window
def clear():
    display_window['text'] = ''

# Deletes the last character in the display window
def delete():
    display_window['text'] = str(display_window['text'])[:-1]


# Creating the display

display_window = Label(main_window,font = 'helvetica 30', anchor = 'e',padx = 8,pady = 8, width = 17)
display_window.grid(row = 1, column = 1,columnspan = 5)


# Creating the buttons

button_1 = Button(main_window,text = '1', command= lambda: add(1),font='helvetica 22',padx = 8,pady = 3)
button_1.grid(row = 5, column = 1,padx = 10,pady = 5)

button_2 = Button(main_window,text = '2', command= lambda: add(2),font='helvetica 22',padx = 8,pady = 3)
button_2.grid(row = 5, column = 2,padx = 5,pady = 5)

button_3 = Button(main_window,text = '3', command= lambda: add(3),font='helvetica 22',padx = 8,pady = 3)
button_3.grid(row = 5, column = 3,padx = 5,pady = 5)

button_4 = Button(main_window,text = '4', command= lambda: add(4),font='helvetica 22',padx = 8,pady = 3)
button_4.grid(row = 4, column = 1,padx = 5,pady = 5)

button_5 = Button(main_window,text = '5', command= lambda: add(5),font='helvetica 22',padx = 8,pady = 3)
button_5.grid(row = 4, column = 2,padx = 5,pady = 5)

button_6 = Button(main_window,text = '6', command= lambda: add(6),font='helvetica 22',padx = 8,pady = 3)
button_6.grid(row = 4, column = 3,padx = 5,pady = 5)

button_7 = Button(main_window,text = '7', command= lambda: add(7),font='helvetica 22',padx = 8,pady = 3)
button_7.grid(row = 3, column = 1,padx = 5,pady = 5)

button_8 = Button(main_window,text = '8', command= lambda: add(8),font='helvetica 22',padx = 8,pady = 3)
button_8.grid(row = 3, column = 2,padx = 5,pady = 5)

button_9 = Button(main_window,text = '9', command= lambda: add(9),font='helvetica 22',padx = 8,pady = 3)
button_9.grid(row = 3, column = 3,padx = 5,pady = 5)

button_0 = Button(main_window,text = '0', command= lambda: add(0),font='helvetica 22',padx = 8,pady = 3)
button_0.grid(row = 6, column = 1,padx = 5,pady = 5)

button_dot = Button(main_window,text = '.', command= lambda: add('.'),font='helvetica 22',padx = 8,pady = 3)
button_dot.grid(row = 6, column = 2,padx = 5,pady = 5)

button_multiply = Button(main_window,text = '*', command= lambda: add('*'),font='helvetica 22',padx = 8,pady = 3)
button_multiply.grid(row = 4, column = 4,padx = 5,pady = 5)

button_divide = Button(main_window,text = '/', command= lambda: add('/'),font='helvetica 22',padx = 8,pady = 3)
button_divide.grid(row = 3, column = 4,padx = 5,pady = 5)

button_add = Button(main_window,text = '+', command= lambda: add('+'),font='helvetica 22',padx = 8,pady = 3)
button_add.grid(row = 5, column = 4,padx = 5,pady = 5)

button_subtract = Button(main_window,text = '-', command= lambda: add('-'),font='helvetica 22',padx = 8,pady = 3)
button_subtract.grid(row = 6, column = 4,padx = 5,pady = 5)

button_left_bracket = Button(main_window,text = '(', command= lambda: add('('),font='helvetica 22',padx = 8,pady = 3)
button_left_bracket.grid(row = 2, column = 1,padx = 5,pady = 5)

button_right_bracket = Button(main_window,text = ')', command= lambda: add(')'),font='helvetica 22',padx = 8,pady = 3)
button_right_bracket.grid(row = 2, column = 2,padx = 5,pady = 5)

button_power = Button(main_window,text = '^', command= lambda: add('**'),font='helvetica 22',padx = 8,pady = 3)
button_power.grid(row = 3, column = 5,columnspan = 2,padx = 5,pady = 5)

button_modulus = Button(main_window,text = 'mod', command= lambda: add('%'),font='helvetica 22',padx = 8,pady = 3)
button_modulus.grid(row = 4, column = 5,columnspan = 2,padx = 5,pady = 5)

button_clear = Button(main_window,text = 'AC', command= clear,font='helvetica 22',bg = 'red', fg = 'white',padx = 24,pady = 3)
button_clear.grid(row = 2, column = 3,columnspan = 2,padx = 5,pady = 5)

button_delete = Button(main_window,text = 'Delete', command= delete,font='helvetica 22',bg = 'purple', fg = 'white',padx = 8,pady = 3)
button_delete.grid(row = 2, column = 5,columnspan = 2,padx = 5,pady = 5)

button_equal = Button(main_window,text = '=', command = answer,font='helvetica 22',bg = 'blue',fg = 'white',padx = 8,pady = 3)
button_equal.grid(row = 6, column = 3,padx = 5,pady = 5)


main_window.mainloop()