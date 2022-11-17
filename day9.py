<<<<<<< HEAD
myDictionary = {"kabir", "Liaquat", "Ahmed"}

for name in myDictionary:
  print(name)
=======
# Exercise 5.2
# input_list = input('Input a list of student scores')

# student_scores = input_list.split()
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score
# print(f'The highest score in the class is: {highest_score}')

# exercise 5.4
# final_number = 0
# for number in range(2, 101, 2):
#     final_number += number
# print(final_number)

#FizzBuzz problem
# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif(number % 3 == 0):
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")

#     else:
#         print(number)


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
final_password = ""
for letter in range(0, nr_letters):
    password_list.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))


for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

for password_item in password_list:
    final_password += password_item
print(final_password)
>>>>>>> 1d870dd4e3b422ae5dbdb0fb0b8b90d44c11e3a1
