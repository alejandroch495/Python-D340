#Variable defined
payHours = float # Hours worked
payRate = float # Rate paid per hour
OVERTIME_RATE = 1.5
payOvertime = float
pay = float # The final calculation of hour x rate

#Need a way to get hours and rate
payHours = float(input("Enter number of hours: "))
payRate = float(input("Enter current rate: "))

#if over 40 hours worked, extract extra hours worked and multiply by overtime rate
if payHours > 40:
    overtimeHours = payHours - 40 
    payOvertime = overtimeHours * (payRate * OVERTIME_RATE)
    pay = (40 * payRate) + payOvertime  

else:
    #Need to calculate pay based on hours x rate if hours is not over 40 hours
    pay = payHours * payRate

#Need to display pay
print("\n Your current pay is ",round(pay,2))