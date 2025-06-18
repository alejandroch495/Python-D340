# Alejandro Chavez
# Chapter 5 exercise 2 
# Company pay calculator ( Re-written )

#set varibles
hours: float = 0
rate: float = 0



def get_input():
    try: # Try getting user input as floats
        hours : float = 0
        rate : float = 0
        hours = float(input("Enter the hours worked: "))
        rate = float(input("Enter the rate : "))
        print(f"""
          The hours worked: {hours} 
          The hourly rate : {rate}""")# This shows the users input as text before the pay is calculated
        return hours, rate # Return both hours and rate to be stored
    except Exception as e: # If input is not a numerical value it will throw an exception
        print("Enter a valid number value.")
        print(e)


def compute_pay(hours, rate) -> float: # This function calculates the pay via the hours, rate variables passed thru
    if hours > 40:
        hours_regular = 40
        hours_overtime = hours - 40
        OVERTIME_RATE = rate * 1.5

        pay = (hours_regular * rate) + (hours_overtime * OVERTIME_RATE)
    else:
        pay = hours * rate
        pay = round(pay,2)
    return pay # Return the pay results


def print_output(pay) -> None:# Display a message to user of total pay
    print(f"""
        The total pay is ${pay:.2f}
""")

def main():
    hours, rate = get_input() # Gets hours and rate input from user
    pay = compute_pay(hours, rate) # pay = the returned pay of compute_pay() via the variables passed thru ( hours and rate )
    print_output(pay) # Displays a message showing the total pay




if __name__ == "__main__":
    main()

""" Output

Enter the hours worked: 40  
Enter the rate : 1

          The hours worked: 40.0
          The hourly rate : 1.0
          The total pay is $40.00


Enter the hours worked: 45
Enter the rate : 10

          The hours worked: 45.0 
          The hourly rate : 10.0
          The total pay is $475.00
      
"""