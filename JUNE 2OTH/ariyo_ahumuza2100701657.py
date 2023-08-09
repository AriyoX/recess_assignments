#create the first set
set1 = {1, 2, 3, 4, 5}

#create the second set
set2 = {4, 5, 6, 7, 8}

#find the length of the first set
set1_length = len(set1)
print("Length of set1:", set1_length)

#find the data type of the first set
set1_data_type = type(set1)
print("Data type of set1:", set1_data_type)

#access items in the first set
for item in set1:
    print(item)

#add items to the first set
set1.add(6)
set1.add(7)
print("Updated set1:", set1)

#add the two sets
combined_set = set1.union(set2)
print("Combined set:", combined_set)
