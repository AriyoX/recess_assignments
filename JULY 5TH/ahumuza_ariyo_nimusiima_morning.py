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

""" a = 5
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
 """



#OOP
""" class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.engine_started = False
    
    def start_engine(self):
        if self.engine_started:
            print("Engine is already running.")
        else:
            self.engine_started = True
            print("Engine started.")
    
    def stop_engine(self):
        if not self.engine_started:
            print("Engine is already stopped.")
        else:
            self.engine_started = False
            print("Engine stopped.")

# Example usage:
my_car = Car("Toyota", "Camry", 2002)
print(f"Car: {my_car.make} {my_car.model} {my_car.year}")

my_car.start_engine()  # Engine started.
my_car.stop_engine()   # Engine stopped.
my_car.start_engine()  # Engine started. """

""" class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount. Please enter a positive value.")
        else:
            self.balance += amount
            print(f"Deposit of {amount} successful. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        elif amount > self.balance:
            print("Insufficient funds. Cannot withdraw.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
    
    def display_balance(self):
        print(f"Account Number: {self.account_number}\nCurrent Balance: {self.balance}")


my_account = BankAccount("123456789")
my_account.deposit(500)            
my_account.withdraw(200)           
my_account.display_balance()       
my_account.deposit(-100)          
my_account.withdraw(400)   
 """


#ecervise: Circle
""" class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        area = 3.14 * (self.radius ** 2)
        return area
    
    def calculate_circumference(self):
        circumference = 2 * 3.14 * self.radius
        return circumference

my_circle = Circle(5)
area = my_circle.calculate_area()
circumference = my_circle.calculate_circumference()

print(f"Radius: {my_circle.radius}")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")

print("////////////////////////////////////////////////////")


#exercise: rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        area = self.length * self.width
        return area
    
    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter


my_rectangle = Rectangle(5, 3)
area = my_rectangle.calculate_area()
perimeter = my_rectangle.calculate_perimeter()

print(f"Length: {my_rectangle.length}")
print(f"Width: {my_rectangle.width}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def calculate_bonus(self):
        bonus = self.salary * (0.5/100)
        return bonus


employee1 = Employee("Employee 1", 150000)
employee2 = Employee("Employee 2", 230000)

bonus1 = employee1.calculate_bonus()
bonus2 = employee2.calculate_bonus()

print(f"{employee1.name} Salary: {employee1.salary}, Bonus: {bonus1}")
print(f"{employee2.name} Salary: {employee2.salary}, Bonus: {bonus2}")

print("////////////////////////////////////////////////////") """

#encapsulation with bank account 
""" class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.account_number = account_number
        self._balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount. Please enter a positive value.")
        else:
            self._balance += amount
            print(f"Deposit of {amount} successful. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        elif amount > self._balance:
            print("Insufficient funds. Cannot withdraw.")
        else:
            self._balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self._balance}")

    def display_balance(self):
        print(f"Account Number: {self.account_number}\nCurrent Balance: {self._balance}")



my_account = BankAccount("123456789", 1000)

my_account.display_balance()  
my_account.deposit(500)       
my_account.withdraw(200)      
my_account.display_balance()  
print(my_account._balance) """


""" #convert temperature(37) to fahrenheit from celsius
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    def get_celsius(self):
        return self._celsius

    def set_celsius(self, celsius):
        self._celsius = celsius

    def to_fahrenheit(self):
        fahrenheit = (self._celsius * 9/5) + 32
        return fahrenheit


temperature = Temperature(37)
celsius = temperature.get_celsius()
fahrenheit = temperature.to_fahrenheit()

print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

print("////////////////////////////////////////////////////")

#assignment 1
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        self.__salary = new_salary

    def increment_pay(self, increment_amount):
        if increment_amount <= 0:
            print("Invalid increment amount.")
        else:
            self.__salary += increment_amount
            print(f"Pay increment applied.")


employee = Employee("Ariyo Ahumuza", 850000)
name = employee.get_name()
salary = employee.get_salary()
print(f"Name: {name}")
print(f"Salary: {salary}")
employee.increment_pay(150000)
new_salary = employee.get_salary()
print(f"Updated Salary: {new_salary}") 
 """

#exercise. demonstrate abstraction using calculating area of a circle and rectangle
""" class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14159 * (self.radius ** 2)
        return area

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area

circle = Circle(5)
circle_area = circle.calculate_area()
print(f"Circle Area: {circle_area}")

rectangle = Rectangle(4, 6)
rectangle_area = rectangle.calculate_area()
print(f"Rectangle Area: {rectangle_area}")


#simple receipting printing program using python
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageDraw, ImageFont

root = Tk()
root.title("Ariyo's Simple Receipt Printing Program")
root.geometry("600x600")

item_fields = [] 

def add_new_item():    
    item_frame = Frame(root)
    item_frame.pack(pady=5)

    name_label = Label(item_frame, text="Item Name:")
    name_label.pack(side=LEFT)
    name_entry = Entry(item_frame)
    name_entry.pack(side=LEFT)

    price_label = Label(item_frame, text="Price:")
    price_label.pack(side=LEFT)
    price_entry = Entry(item_frame)
    price_entry.pack(side=LEFT)

    quantity_label = Label(item_frame, text="Quantity:")
    quantity_label.pack(side=LEFT)
    quantity_entry = Entry(item_frame)
    quantity_entry.pack(side=LEFT)

    item_fields.append((name_entry, price_entry, quantity_entry))

def print_receipt():
    receipt = ""

    for name_entry, price_entry, quantity_entry in item_fields:
        name = name_entry.get()
        price = price_entry.get()
        quantity = quantity_entry.get()

        if not name or not price or not quantity:
            messagebox.showerror("Error", "Please enter all item details")
            return

        try:
            price = float(price)
            quantity = int(quantity)
            if price <= 0 or quantity <= 0:
                raise ValueError("Price and quantity must be greater than zero.")
            total = price * quantity
            receipt += f"Item: {name}\tPrice: {price}\tQuantity: {quantity}\tTotal: {total}\n"
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return

    if receipt:
        top = Toplevel()
        top.geometry("500x400")
        top.config(background="white")

        receipt_label = Label(top, text="RECEIPT")
        receipt_label.pack()
        receipt_label.config(background="white")

        receipt_text = Text(top, height=20, width=60)
        receipt_text.pack()
        receipt_text.insert(END, receipt)
        receipt_text.config(state=DISABLED)

        save_button = Button(top, text="Save Receipt", command=lambda: save_receipt(receipt))
        save_button.pack(side=LEFT, pady=10, padx=5)


def save_receipt(receipt):
    save_file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("Image Files", "*.png")])
    if save_file_path:
        file_extension = save_file_path.split(".")[-1].lower()

        if file_extension == "txt":
            with open(save_file_path, "w") as file:
                file.write(receipt)
            messagebox.showinfo("Success", "Receipt saved as a text file.")
        elif file_extension == "png":
            save_receipt_image(save_file_path, receipt)
        else:
            messagebox.showerror("Error", "Invalid file format. Please choose a text file (.txt) or an image file (.png).")

def save_receipt_image(file_path, receipt):
    image_width = 500
    image_height = 400

    receipt_image = Image.new("RGB", (image_width, image_height), color="white")
    draw = ImageDraw.Draw(receipt_image)
    font = ImageFont.truetype("arial.ttf", size=12)

    lines = receipt.split("\n")
    y = 10

    for line in lines:
        draw.text((10, y), line, font=font, fill="black")
        y += 20

    receipt_image.save(file_path)
    messagebox.showinfo("Success", "Receipt saved as an image file.")

add_item_button = Button(root, text="Add New Item", command=add_new_item)
add_item_button.pack(pady=5)

print_button = Button(root, text="Print Receipt", command=print_receipt)
print_button.pack(pady=10)

root.mainloop() """

#
import re
pattern = r'apple'
text = 'I have an apple and an orange.'
match = re.search(pattern, text)
if match:
    print('Pattern found!')
else:
    print('Pattern not found.')


pattern = r'\d+'  #matches one or more digits
text = 'I have 3 apples and 2 oranges.'
matches = re.findall(pattern, text)
print(matches)


pattern = r'\s+'  #matches one or more whitespace characters
text = 'I have apples   and     oranges.'
words = re.split(pattern, text)
print(words)


pattern = r'(\d+)-(\d+)-(\d+)'  #matches date pattern in format: yyyy-mm-dd
text = 'Today is 2023-07-05.'
match = re.search(pattern, text)
if match:
    year = match.group(1)
    month = match.group(2)
    day = match.group(3)
    print(f"Year: {year}, Month: {month}, Day: {day}")


#iterators and generators
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

#example
my_iter = MyIterator([1, 2, 3, 4, 5])
for num in my_iter:
    print(num)

def my_generator(data):
    for item in data:
        yield item

#example usage
my_iter = my_generator([1, 2, 3, 4, 5])
for num in my_iter:
    print(num)

#assignment a7
#Show a context manager for file handling that automatically opens and closes a file.
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

#example 
with FileManager('example.txt', 'w') as file:
    file.write('Hello, world!')


#Show a context manager for managing a database connection
import psycopg2

class DatabaseManager:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def __enter__(self):
        self.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
        )
        return self.connection

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()

#example
with DatabaseManager('localhost', '5432', 'mydatabase', 'myuser', 'mypassword') as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

#Show a Multithreading and multiprocessing for running a function for different amounts of time
import threading
import multiprocessing
import time

def run_function(duration):
    print(f"Function started. Running for {duration} seconds.")
    time.sleep(duration)
    print(f"Function completed after {duration} seconds.")

#multithreading example
def run_multithreading():
    durations = [1, 2, 3]
    threads = []

    for duration in durations:
        thread = threading.Thread(target=run_function, args=(duration,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

# Multiprocessing example
def run_multiprocessing():
    durations = [1, 2, 3]
    processes = []

    for duration in durations:
        process = multiprocessing.Process(target=run_function, args=(duration,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

#example
print("Multithreading:")
run_multithreading()

print("Multiprocessing:")
run_multiprocessing()

















