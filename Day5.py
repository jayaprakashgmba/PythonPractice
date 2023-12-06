#day5


#for loop  example (fot xxxxxx in xxxxxxs)

# fruits = ["mango", "goa", "banana"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit[0])
#     print(fruits[0])
#     print(fruit + "lemon")
# print(fruits)

# syntax
# student_score = input("enter your score:")
# for n in range(0, len(student_score)):
#     student_score[n] = int(student_score[n])
# print(student_score)


# student_scores = input("enter your sccores:")
# heighest_score = 0
# for score in heighest_score:
#     if score > heighest_score:
#         heighest_score = score
# print (f"your heightest score {heighest_score}") 



# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# # password = ""
# for char in range(1, nr_letters +1):
#     password += random.choice(letters)

# for char in range(1, nr_symbols + 1):
#     password += random.choice(symbols)

# for char in range(1, nr_numbers + 1):
#     password += random.choice(numbers)
# print(password)

# hardway
# password_list = []

# for char in range(1, nr_letters + 1):
#     password_list.append(random.choice(letters))
# for char in range(1, nr_numbers + 1):
#     password_list += random.choice(numbers)
# for char in range(1, nr_symbols):
#     password_list += random.choice(symbols)

# # print(password_list)
# random.shuffle(password_list)
# # print(password_list)

# password = ""
# for char in password_list:
#     password  += char

# print(f"your password {password}")



