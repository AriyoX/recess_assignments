#STRINGS
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



