"""
Assignment #1

1. Create two variables, one with your name and one with your age.
2. Create a function which prints your data as a string.
3. Create a function which prints ANY data (two parguments) as one string.
4. Create a function which calculates and returns the number of decades you already lived.
"""
"""Raw Attempt"""
#Variable Declaration
#Achieves Task #1
my_name = "Jessi"
my_age = 23

#Printing Data
#Achieves Task #2
print(my_name, str(my_age))

#Printing Any Data
#Achieves Task #3
your_name = input("Please enter your name: ")
your_age = input("Please enter your age: ")
print(your_name, str(your_age))

#Calculating Decades Past
#Achieves Task #4

def decade_calculator(my_age):
    decades = float(my_age / 10)
    print("You have been alive for ", str(decades), "decades!")

decade_calculator(my_age)
    
"""Honed Attempt After Viewing Solution"""
#Variable Declaration
#Achieves Task #1
#NOTES: Didn't realize he was asking for us to input it in the initial assignment criteria.
my_name = input("What is your name, self? ")
my_age = input("What is your age, self? ")

#Printing Data
#Achieves Task #2
#NOTES: He makes everything a function. Cleaned this up, and did that.
def print_my_data():
    print(my_name + ", " + my_age)

print_my_data()

#Printing Any Data
#Achieves Task #3
#NOTES: Functions again.
your_name = input("Please enter your name: ")
your_age = input("Please enter your age: ")

def print_data(your_name, your_age):
    print(your_name + ", " + your_age)

#Calculating Decades Past
#Achieves Task #4
#NOTES: About the same.

def decade_calculator(age):
    decades_lived = float(age / 10)
    return decades_lived

decades=decade_calculator(float(my_age))
print("You have been alive for ", str(decades), "decades!")