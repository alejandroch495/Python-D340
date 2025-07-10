# Chapter 2 Exercise 1 - Alejandro Chavez
# Pay Rate Calculator
"""
The following are the requirments for the program
----------------------------------------------------
Write a program to prompt the user for hours and rate per hour to compute gross pay.
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
Put at least two outputs (results after you run your code) at the end of your code as a multi-line comment.
-----------------------------------------------------

Initial scope variables needed : [list of known itial variables]

hours => float
rate => float
pay => float

In-progress variables : [list of new variables needed]

dividerLine = string

"""
#Variable defined
payHours = float # Hours worked
payRate = float # Rate paid per hour
pay = float # The final calculation of hour x rate
dividerLine = "-------------------------------" # Used to create a divider line in the console window to provide a clearer view

#Need a way to get hours
payHours = float(input("Enter number of hours: "))

#Need a way to get rate
payRate = float(input("Enter current rate: "))

#Need to calculate pay based on hours x rate
pay = payHours * payRate

#Need to display pay
print("\n Your current pay is \n",pay)

#Extra: Want to display to user the "rate" and "hours"
"""
example text display

"pay info"
-------------------------------
hours: #
rate: #
-------------------------------

"""
print(dividerLine)
print("Hours:", payHours,"\nRate:", payRate)
print(dividerLine)
"""
Output 1

Enter number of hours: 40
Enter current rate: 2

 Your current pay is
 80.0
-------------------------------
Hours: 40.0
Rate: 2.0
-------------------------------

Output 2 

Enter number of hours: 25
Enter current rate: 8

 Your current pay is
 200.0
-------------------------------
Hours: 25.0
Rate: 8.0
-------------------------------
"""
 

 

