#Variable defined
payHours = float # Hours worked
payRate = float # Rate paid per hour
OVERTIME_RATE = 1.5
payOvertime = float
pay = float # The final calculation of hour x rate

#Need a way to get hours and rate
payHours = float(input("Enter number of hours: "))

#Need a way to get rate
payRate = float(input("Enter current rate: "))

#Need to calculate pay based on hours x rate
pay = payHours * payRate

#Need to display pay
print("\n Your current pay is \n",pay)