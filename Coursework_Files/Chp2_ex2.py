# Alejandro Chavez  
# Chapter 2 Exercise 2
# Change to dollars


# Write a program that prompts the user to enter how many pennies they have. Then convert pennies to dollars and cents.


# Defining Variables
pennies = int
dollars = float

# Get user input on how many pennies
pennies = int(input("Enter the amount of pennies :"))

# Get amount in dollars
dollars = pennies // 100


# Get remaining pennies that don't fint into dollars
pennies = pennies % 100

print("$" , str(dollars) + "." + "%02d" % pennies)

"""
output 1

Enter the amount of pennies :50468
$504.68

output 2

Enter the amount of pennies :111
$ 1.11
"""