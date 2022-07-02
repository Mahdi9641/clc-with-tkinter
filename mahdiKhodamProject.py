# Import required modules
import tkinter.font as font
from tkinter import *
from tkinter import messagebox

import modul_cal

root = Tk()              #harchi ke to on panjare tkinter anjam mishe ro tosh minvisim

# Assigning it the desired geometry
root.geometry("420x440")   #size

# Assigning the name of our window
root.title("Mahdi_Khodam_calculator")

root.configure(bg="grey")  #background

# Assigning it the capability to
# be resizable (It is default)
root.resizable(0,0)

# Creating a StringVar to take
# the text entered in the Entry widget
inp = StringVar()
myFont = font.Font(size=20)


# Creating an Entry widget to get the
# mathematical expression
# And also to display the results
screen = Entry(root, text=inp, width=30,
               justify='left', font=(20), bd=4, bg="black", fg="white")

# We will use a grid like structure
screen.grid(row=0, columnspan=4, padx=18,
            pady=16, ipady=5)

# Key matrix contains all the required the keys
key_matrix = [["c", "(", ")", "/"],
              ["7", "8", "9", "*"],
              ["4", "5", "6", "-"],
              ["1", "2", "3", "+"],
              ["!", 0, ".", "="]]

#>>>>>>>>>>>>>>>>>>>>>>>>>>menubar>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def about():
    messagebox.showinfo('About'," \n Created by MahdiKhodam \n \n  github :\n  https://github.com/Mahdi9641/tutorials")


menubar = Menu(root,bg="black",fg="grey")

filemenu = Menu(menubar, tearoff=0,bg="red",fg="black")
filemenu.add_command(label="Cut", accelerator="Ctrl+X" )
filemenu.add_command(label="Copy",accelerator="Ctrl+C" )
filemenu.add_command(label="Paste",accelerator="Ctrl+V")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="Edit", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0,bg="red",fg="black")
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About", command=about)

root.config(bg="grey",menu=menubar)




# Creating a dictionary for the buttons
btn_dict = {}

# Variable to store our results
ans_to_print = 0


# Defining the function for calculation
def Calculate(event):
    # getting the name of the button clicked
    button = event.widget.cget("text")

    # Referring the global values
    global key_matrix, inp, ans_to_print

    try:

        if button == "c":  # Clear Button
            inp.set("")

        elif button == "!":  # Factorial
            def fact(n):
                return 1 if n == 0 else n * fact(n - 1)

            inp.set(str(fact(int(inp.get()))))

        elif button == "=":  # Showing The Results
            ans_to_print = str(modul_cal.ob.solve((inp.get())))
            inp.set(ans_to_print)
            print("the resault is = " + ans_to_print)

            with open("m.txt", "a+") as file:

                data = file.read()
                file.write("\n")
                file.write(" the calculator resault is = " + ans_to_print)


        # You may add many more operations

        else:
            # Displaying the digit pressed on screen
            inp.set(inp.get() + str(button))

    except:
        # In case invalid syntax given in expression
        inp.set("Wrong Operation")
        print("WRONG!!!!")


# Creating the buttons using for loop

# Number of rows containing buttons
for i in range(len(key_matrix)):
    # Number of columns
    for j in range(len(key_matrix[i])):
        # Creating and Adding the buttons to dictionary
        btn_dict["btn_" + str(key_matrix[i][j])] = Button(
            root, bd=1, text=str(key_matrix[i][j]), font=myFont, bg="yellow", fg="black")

        # Positioning buttons
        btn_dict["btn_" + str(key_matrix[i][j])].grid(
            row=i + 1, column=j, padx=5, pady=5, ipadx=5, ipady=5)

        # Assigning an action to the buttons
        btn_dict["btn_" + str(key_matrix[i][j])].bind('<Button-1>', Calculate)

# Running the main loop
root.mainloop()
