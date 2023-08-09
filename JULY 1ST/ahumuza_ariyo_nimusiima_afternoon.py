""" #STRINGS
print("STRINGS")
print()
print()
#exercise one
text = "Hello, World!"
length = len(text)
print("The length of the string is:", length)

#exercise two
text = "Hello"
for character in text:
    print(character)

#exercise 
text = "Hello, World!"
slice1 = text[0:5]  # Slicing from index 0 to 4 (exclusive)
slice2 = text[7:]   # Slicing from index 7 to the end of the string
slice3 = text[:5]   # Slicing from the beginning to index 4 (exclusive)
print(slice1)
print(slice2)
print(slice3)


#DICTIONARIES
print("DICTIONARIES")
print()
print()
my_dictionary = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

#exercise one: using the values() method to return a list of all values in the dictionary
values_list = list(my_dictionary.values())
print("List of values:", values_list)

#exercise two: checking if a key exists in the dictionary
key = "age"
if key in my_dictionary:
    print("Key '{}' exists in the dictionary.".format(key))
else:
    print("Key '{}' does not exist in the dictionary.".format(key))

#exercise three: changing dictionary items (updating)
my_dictionary["city"] = "San Francisco"
print("Updated dictionary:", my_dictionary)

#exercise four: adding and removing dictionary items
my_dictionary["gender"] = "Male"  #adding a new key-value pair
print("Dictionary after adding item:", my_dictionary)

del my_dictionary["age"]  #removing the "age" key and its value
print("Dictionary after removing item:", my_dictionary)

#exercise five: looping through a dictionary and nesting dictionaries
for key, value in my_dictionary.items():
    print(key + ":", value)

#nesting dictionaries
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 32}
}
print("Nested dictionary:", nested_dict)
 """

#Exercise 1
#1
""" names = ["Ariyo", "Conrad", "Ssenono", "Ojok", "Cronnie"]
print(names[1]) 

#2
names[0] = "Ahumuza"
print(names) 

#3
names.append("Ssematimba")
print(names) 

#4
names.insert(2, "Bathel")
print(names) 

#5
del names[3]
print(names) 

#6
print(names[-1]) 

#7
new_list = [1, 2, 3, 4, 5, 6, 7]
print(new_list[2:5])  

#8
countries = ["USA", "Canada", "Mexico", "Germany", "France"]
countries_copy = countries.copy()
print(countries_copy) 

#9
for country in countries:
    print(country)

#10
animals = ["hen", "cat", "dog", "lion", "rat"]
animals.sort()  #ascending order
print(animals)  

animals.sort(reverse=True)  #descending order
print(animals)  

#11
for animal in animals:
    if 'a' in animal:
        print(animal)


#12
first_names = ["Ariyo"]
last_names = ["Ahumuza"]
full_names = first_names + last_names
print(full_names)  


#Exercise 2
#1
x = ("samsung", "iphone", "tecno", "redmi")
favorite_phone_brand = x[0]
print(favorite_phone_brand) 

#2
print(x[-2])  

#3
x = list(x)
x[1] = "itel"
x = tuple(x)
print(x)  

#4
x = x + ("Huawei",)
print(x) 

#5
for phone in x:
    print(phone)

#6
x = x[1:]
print(x) 

#7
ugandan_cities = tuple(["Kampala", "Entebbe", "Jinja", "Gulu"])
print(ugandan_cities) 

#8
a, b, c, d = ugandan_cities
print(a)  
print(b)  
print(c)  
print(d)  

#9
print(ugandan_cities[1:4]) 

#10
first_names = ("Ariyo")
last_names = ("Nimusiima")
full_names = first_names + last_names
print(full_names)  

#11
colors = ("red", "green", "blue")
multiplied_colors = colors * 3
print(multiplied_colors) 

#12
this_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = this_tuple.count(8)
print(count_8) 


#Exercise 3
#1
beverages = set(["coffee", "soda", "gatorade"])
print(beverages) 

#2
beverages.add("water")
beverages.add("smoothie")
print(beverages) 

#3
mySet = {"oven", "kettle", "microwave", "refrigerator"}
if "microwave" in mySet:
    print("Microwave is present in the set.")
else:
    print("Microwave is not present in the set.")

#4
mySet.remove("kettle")
print(mySet) 

#5
for item in mySet:
    print(item)

#6
mySet = {1, 2, 3, 4}
myList = [5, 6]
mySet.update(myList)
print(mySet) 

#7
ages = {21}
first_names = {"Ariyo"}
combined_set = ages.union(first_names)
print(combined_set)  


#Exercise 4
#1
num = 10
text = "Hello"
concatenated = str(num) + text
print(concatenated)  

#2
txt = "     Hello,    Uganda!    "
trimmed = txt.strip()
trimmed = trimmed.replace(" ", "")
print(trimmed) 

#3
txt = "Hello, Uganda!"
uppercase = txt.upper()
print(uppercase)  

#4
txt = "Hello, Uganda!"
replaced = txt.replace("U", "V")
print(replaced)  

#5
y = "I am proudly Ugandan"
range_of_chars = y[1:4]
print(range_of_chars)  

#6
x = 'All "Data Scientists" are cool!'
print(x) 


#Exercise 5
#1
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}
print(Shoes["size"])  

#2
Shoes["brand"] = "Adidas"
print(Shoes)  

#3
Shoes["type"] = "sneakers"
print(Shoes)  

#4
keys_list = list(Shoes.keys())
print(keys_list)  

#5
values_list = list(Shoes.values())
print(values_list)  

#6
if "size" in Shoes:
    print("Key 'size' exists in the dictionary.")
else:
    print("Key 'size' does not exist in the dictionary.")

#7
for key, value in Shoes.items():
    print(key + ": " + str(value))

#8
del Shoes["color"]
print(Shoes)  

#9
Shoes.clear()
print(Shoes)  

#10
original_dict = {"name": "Ariyo", "age": 21}
copied_dict = original_dict.copy()
print(copied_dict)  

#11
person = {
    "name": "Ariyo",
    "age": 21,
    "address": {
        "street": "Ggaba Rd",
        "city": "Kampala",
        "country": "Uganda"
    }
}
print(person) 
 """

""" Exception handling is a crucial aspect of programming in Python. It enables developers to handle errors and exceptional situations that may occur during program execution. By using try-catch blocks, developers can prevent program crashes, provide meaningful error feedback, and ensure program stability.
Python supports various types of errors, including compile-time, runtime, and logical errors. Exception handling allows you to catch and handle these errors gracefully, improving the overall robustness of your code.
In Python, the try block contains the potentially problematic code, and if an error occurs, it throws an exception. The exception is caught by the appropriate catch block, which handles the error by executing specific error-handling logic. Python allows multiple catch blocks to handle different types of exceptions.
Python's exception handling mechanism also includes the finally block, which is executed regardless of whether an exception occurred or not. It is useful for tasks such as resource cleanup.
Exception handling in Python is essential for creating stable and reliable applications. It helps in preventing abrupt program terminations, providing informative error messages, and enhancing the overall user experience. By using exception handling effectively, you can write robust Python code that gracefully handles errors and exceptional situations. """

#Example 1: Handling a specific exception
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)

#Handling division by zero error
except ZeroDivisionError:  
    print("Error: Cannot divide by zero.")

#Handling invalid input error
except ValueError:  
    print("Error: Invalid input. Please enter a valid number.")

#Example 2: Using the 'else' clause
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    else:
        print("Age:", age)

except ValueError as ve:
    print("Error:", str(ve))

#Example 3: Using the 'finally' clause
try:
    file = open("example.txt", "r")
    content = file.read()
    print("File content:", content)

except FileNotFoundError:
    print("Error: File not found.")

finally:
    file.close()
    print("File closed.")

#Example 4: Raising an exception manually
def calculate_percentage(marks, total):
    if total == 0:
        raise ValueError("Total marks cannot be zero.")
    return (marks / total) * 100

try:
    marks = int(input("Enter your marks: "))
    total_marks = int(input("Enter total marks: "))
    percentage = calculate_percentage(marks, total_marks)
    print("Percentage:", percentage)

except ValueError as ve:
    print("Error:", str(ve))

'''
File handling in Python refers to the ability to work with files, such as reading from or writing to them. It allows programmers to manipulate data stored in files, making it an essential aspect of many applications that deal with persistent data storage.

File Handling Operations:
File handling operations include reading data from a file, writing data to a file, appending data to an existing file, and modifying or deleting files. These operations enable interaction with files for various purposes, such as data storage, configuration files, logs, and more.

Opening a File in Python:
To work with a file, you need to open it first. Python provides the open() function to open a file. It takes the file name along with the desired mode as parameters and returns a file object that represents the opened file.

Various Modes of File:
Python supports different modes for file handling, which determine how the file can be accessed. Some commonly used file modes are:
r: open an existing file for a read operation.
w: open an existing file for a write operation. If the file already contains some data then it will be overridden but if the file is not present then it creates the file as well.
a:  open an existing file for append operation. It wontt override existing data.
r+: To read and write data into the file. The previous data in the file will be overridden.
w+: To write and read data. It will override existing data.
a+: To append and read data from the file. It wontt override existing data

File Handling Process:
1)Open the file using the open() function and specifying the desired mode.
2)Perform the required file handling operations, such as reading or writing data.
3)Close the file using the close() method of the file object to release system resources and ensure data integrity.

Types of Files:
Python supports various types of files, including text files, binary files, CSV (Comma-Separated Values) files, JSON (JavaScript Object Notation) files, and more. Each type has its specific format and purpose, and Python provides appropriate libraries and modules to handle these file types effectively.

Advantages of Using Files:
1) Data Persistence: Files allow data to be stored and retrieved even after the program terminates. This enables the long-term storage and retrieval of information.
2) Data Sharing: Files facilitate data sharing between different programs or systems. They provide a common medium for data exchange, allowing data to be accessed and processed by multiple applications.
3) Data Backup: Files serve as a means of data backup, allowing important information to be saved and restored when needed.
4) Data Organization: Files provide a structured way to organize and manage data. They can be organized into directories and subdirectories, enabling logical grouping and easy retrieval.
5) Data Processing: Files enable large-scale data processing. By reading data from files, performing operations, and writing back the results, complex data processing tasks can be efficiently handled.
'''

#Example 1: Reading content in a file

#open the file in read mode
file = open("example.txt", "r")
#read the contents of the file
content = file.read()
#print the content
print(content)
#close the file
file.close()

#Example 2: Writing content to a file

#open the file in write mode
file = open("example.txt", "w")
#write data to the file
file.write("Hello, World!")
#close the file
file.close()

#Example 3: Appending data to a file

#open the file in append mode
file = open("example.txt", "a")
#append data to the file
file.write("\nThis is additional content.")
#close the file
file.close()

#Example 4: Reading data in the file line by line

#open the file in read mode
file = open("example.txt", "r")
#read the file line by line
lines = file.readlines()
#print each line
for line in lines:
    print(line)
#close the file
file.close()














































