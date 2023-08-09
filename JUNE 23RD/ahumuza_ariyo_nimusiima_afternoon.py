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
names = ["Ariyo", "Conrad", "Ssenono", "Ojok", "Cronnie"]
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













































