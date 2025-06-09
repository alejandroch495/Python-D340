# Alejandro Chavez   
# Chapter 4 exercise 2
# Company pay calculator

#set varibles
from random import randrange


pay : float = 0
rate : float = 0
hours : float = 0
OVERTIME_RATE : float = 1.5
MAX_BASE_WORK_HOURS : float = 40
companyName : str = ""
overtimePay : float = 0
overtimeHours : float = 0
overtimeRate : float = 0 
is_running : bool = True
documentNum : int = 0

while is_running:
    try: #try running program
        companyName = input("Enter company name : ").strip()
        companyName = companyName.replace(companyName[0],companyName[0].upper(),1)
        hours = float(input("Enter Hours: "))
        rate = float(input("Enter Rate: "))

        # Overtime pay calculations
        if hours > MAX_BASE_WORK_HOURS:
            overtimeHours = round(hours - MAX_BASE_WORK_HOURS,2)
            hours = MAX_BASE_WORK_HOURS
            overtimeRate = round(OVERTIME_RATE * rate,2)
            pay = round((rate * hours)+(overtimeHours * overtimeRate),2)
        # Regular pay calculations
        else:
            pay = hours * rate

         # Generation of random document number between 1000-2000   
        documentNum = randrange(1000,2000)


        # Display Info back to user
        print(f"\nComapny: {companyName}")
        print(f"Hours: {hours + overtimeHours:.2f}")
        print(f"Rate: {rate:.2f}")
        print("*" * 30)
        print(f"Your document number is: {documentNum}")
        print(f"Company Name: {companyName}")
        print(f"Your {companyName} gross pay is {pay:.2f} dollars.")
        
        # Exit program
        is_running = False
    except Exception as e:
        print("Error below \n\n",e)

"""
Output

Enter company name : test
Enter Hours: 45
Enter Rate: 10

Comapny: Test
Hours: 45.00
Rate:10.00
******************************
Your document number is: 1665
Company Name: Test
Your Test gross pay is 475.00 dollars.



Enter company name : google
Enter Hours: 41
Enter Rate: 1

Comapny: Google
Hours: 41.00
Rate: 1.00
******************************
Your document number is: 1690
Company Name: Google
Your Google gross pay is 41.50 dollars.



Enter company name : apple
Enter Hours: 100
Enter Rate: 1

Comapny: Apple
Hours: 100.00
Rate: 1.00
******************************
Your document number is: 1642
Company Name: Apple
Your Apple gross pay is 130.00 dollars.

"""