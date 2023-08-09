# Create the first set
set1 = {1, 2, 3, 4, 5}

# Create the second set
set2 = {4, 5, 6, 7, 8}

# Find the length of the first set
set1_length = len(set1)
print("Length of set1:", set1_length)

# Find the data type of the first set
set1_data_type = type(set1)
print("Data type of set1:", set1_data_type)

# Access items in the first set
for item in set1:
    print(item)

# Add items to the first set
set1.add(6)
set1.add(7)
print("Updated set1:", set1)

# Combine the two sets
combined_set = set1.union(set2)
print("Combined set:", combined_set)

# Create a list
list1 = [1, 2, 3, 4, 5]

# Find the length of the list
list1_length = len(list1)
print("Length of list1:", list1_length)

# Access items in the list
for item in list1:
    print(item)

# Add items to the list
list1.append(6)
list1.append(7)
print("Updated list1:", list1)

# Concatenate two lists
list2 = [8, 9, 10]
concatenated_list = list1 + list2
print("Concatenated list:", concatenated_list)

# Create a tuple
tuple1 = (1, 2, 3, 4, 5)

# Find the length of the tuple
tuple1_length = len(tuple1)
print("Length of tuple1:", tuple1_length)

# Access items in the tuple
for item in tuple1:
    print(item)
