'''
print("ENTER AGE PROGRAM")
age = int(input("Enter age: "))
if(age < 18):
	print("You are underage")
elif(age >= 18 and age <= 65):
	print("You are an adult")
else:
	print("You are a senior citizen")
        
print("WORKING WITH LOOPS")
numbers = [1, 2, 3, 4, 5]
for number in numbers:
	print (number)
	
number_size = 0
while number_size < 5:
	print (number_size)
	number_size += 1

#search for a target number in a list
numbers = [2, 5, 8, 12, 9, 15, 7]
target = 9

for num in numbers:
    if num == target:
        print("Target number found!")
        break
else:
    print("Target number not found.")

#print only odd numbers from a list
numbers = [1, 4, 3, 7, 2, 6, 9]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)


print("MENTAL HEALTH PROGRAM USING DICTIONARIES AND EXCEPTION HANDLINGp")
valid_input = False
#flag to keep track of whether the user has entered a valid input for their mental health rating

while not valid_input:
    try:
        rating = int(input("Please rate your mental health from 1 to 10: "))
        if 1 <= rating <= 10:
            valid_input = True
        else:
            print("Invalid rating. Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input. Please enter a number.")

prompts = {
    1: "You're feeling really down. Remember, it's okay to ask for help.",
    2: "You're not feeling great. Reach out to someone you trust.",
    3: "You're feeling a bit low. Take some time for self-care.",
    4: "You're feeling okay, but there's room for improvement.",
    5: "You're feeling neutral. Consider engaging in activities you enjoy.",
    6: "You're feeling good. Keep up the positive mindset!",
    7: "You're feeling quite positive. Maintain your well-being.",
    8: "You're feeling great! Keep doing what makes you happy.",
    9: "You're feeling amazing! Share your positive energy with others.",
    10: "You're feeling fantastic! Keep up the excellent mental well-being!"
}

print(prompts[rating])

'''
a = 5
b = 3

result_add = a + b
print(result_add)

result_sub = a - b
print(result_sub)

result_mul = a * b
print(result_mul)

result_div = a / b
print(result_div)

result_floor_div = a // b
print(result_floor_div)

result_modulo = a % b
print(result_modulo)

result_exp = a ** b
print(result_exp)

#logical operators
result_eq = a == b
print("Equality:", result_eq)  

result_ineq = a != b
print("Inequality:", result_ineq) 

result_gt = a > b
print("Greater than:", result_gt)  

result_lt = a < b
print("Less than:", result_lt)  

result_gte = a >= b
print("Greater than or equal to:", result_gte) 

result_lte = a <= b
print("Less than or equal to:", result_lte)

a = True
b = False

result_and = a and b
print("Logical AND:", result_and) 

result_or = a or b
print("Logical OR:", result_or) 

result_not_a = not a
print("Logical NOT (a):", result_not_a) 

result_not_b = not b
print("Logical NOT (b):", result_not_b)  

#assignment operators
a = 5
b = 3

#addition assignment
a += b
print("Addition Assignment:", a) 

#subtraction assignment
a -= b
print("Subtraction Assignment:", a) 

#multiplication assignment
a *= b
print("Multiplication Assignment:", a)

#division assignment
a /= b
print("Division Assignment:", a)  

#floor division assignment
a //= b
print("Floor Division Assignment:", a) 

#modulo assignment
a %= b
print("Modulo Assignment:", a) 

#exponentiation assignment
a **= b
print("Exponentiation Assignment:", a)  

#membership operators
x = 10
y = 3

#is
result_is = x is y
print("Identity Operator (is):", result_is)

#in
numbers = [1, 2, 3, 4, 5]
result_in = 3 in numbers
print("Membership Operator (in):", result_in)  

#bitwise Operators
p = 5  #0101 in binary
q = 3  #0011 in binary

# Bitwise AND
result_and = p & q
print("Bitwise AND:", result_and)  

# Bitwise OR
result_or = p | q
print("Bitwise OR:", result_or)  

# Bitwise XOR
result_xor = p ^ q
print("Bitwise XOR:", result_xor) 

# Bitwise NOT
result_not_p = ~p
print("Bitwise NOT (p):", result_not_p)  

result_not_q = ~q
print("Bitwise NOT (q):", result_not_q)  

# Bitwise Left Shift
result_left_shift = p << 1
print("Bitwise Left Shift:", result_left_shift)  

# Bitwise Right Shift
result_right_shift = p >> 1
print("Bitwise Right Shift:", result_right_shift)  


#Calculator Program with GUI interface
#make the title of the calculator program e.g. ARIYO SIMPLE CALC

from tkinter import *

def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    global equation_text
    try:
        #eval parses the equation passed in
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("SYNTAX ERROR")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("ARITHMETIC ERROR")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

#create the window
window = Tk()
window.title("Ariyo's Simple Calculator")
window.geometry("600x600")

#variable to store the equation
equation_text = ""
equation_label = StringVar()

#display for numbers being entered in
label = Label(window, textvariable=equation_label, font=('Digital-7', 32), bg="white", width=20, height=3, padx=10, pady=10, borderwidth=1, relief="solid")
label.pack()

#frame for the buttons
frame = Frame(window)
frame.pack()

#assigning buttons in the frame with their respective functions and commands
#lambda used to delay execution of the function until button is clicked
button1 = Button(frame, text=1, height=4, width=9, font=35, command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35, command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35, command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35, command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35, command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35, command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35, command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35, command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35, command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35, command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35, command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35, command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35, command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35, command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35, command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35, command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=12, font=35, command=clear)
clear.pack()


window.mainloop()



