# Alejandro Chavez
# Chapter 5 exercise 1
# Pay calculator rewritten with functions

hours = 0
rate = 0 
pay = 0

# Main function
def main():
    #set rate and hours
    rate , hours = get_input()
    #set pay
    pay = calculate_pay(hours, rate)
    #show pay
    print_pay(pay)

# Get user input for hours and rate
def get_input() -> float:
    hours = float(input("Enter hours: "))
    rate = float(input("Enter rate: "))
    return rate, hours

def calculate_pay(hours : float, rate: float) -> float:
    pay = hours * rate
    return pay

def print_pay(pay) -> None:
    print(f"Your pay is : ${pay:.2f}")

main()



"""
output 


Enter hours: 40
Enter rate: 1
Your pay is : $40.00


Enter hours: 20
Enter rate: 20
Your pay is : $400.00
"""