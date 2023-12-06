version="311.4"
print(version)



#Data Type

num_integer = 5
num_float = 3.14
text = "Python is fun"
my_list = [1, 2, 3]
my_dict = {'key': 'value'}

#List and indexing 
my_list = [10, 20, 30, 40]
print(my_list[0])  # Outputs: 10


#Conditional statement
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")


#Loops
for i in range(5):
    print(i)  # Outputs: 0, 1, 2, 3, 4

while x > 0:
    print(x)
    x -= 1


#Function
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Outputs: Hello, Alice!


#Modules and Libraries
import math
print(math.sqrt(16))  # Outputs: 4.0


#user inputs
name = input("Enter your name: ")
print(f"Hello, {name}!")


#String manupalition
name = "John"
greeting = f"Hello, {name}!"
print(greeting)  # Outputs: Hello, John!
