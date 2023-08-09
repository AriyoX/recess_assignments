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
