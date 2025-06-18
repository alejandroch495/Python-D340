# Alejandro Chavez
# Chapter 6 - Exercise 5
# Company pay program
from random import randint




COMPANYLIST : list[str] = ['Apple', 'Microsoft', 'Google','Amazon', 'Uber', 'Facebook']
attempts : int = 0
rate : float = 0.0
pay : float = 0.0
RATE_OVERTIME = 1.5
hours: float = 0
document_numbers : list[int] = []




# This function formats input so the first letter is always capitolized
def format_input(input):
    '''##### Turns input into a formated string that always has the first letter capitolized.
    ### Example : "apPle" -> "Apple"'''
    if input != "":
        ending_letters : str = ""
        first_letter, *remaining_letters = input
        for i in remaining_letters:
            ending_letters += i
        return_var = first_letter.capitalize() + ending_letters
        return return_var
    else: 
        return " "




def get_user_company_name():
    '''### Saves users entered company name.
    If incorrect company name is entered twice it will output a list of options availible'''
    global attempts
    print()

    user_input = input('Enter Company Name : ').strip().lower()

    formated_user_input = format_input(user_input)

    if formated_user_input in COMPANYLIST:
        return formated_user_input
    
    if formated_user_input not in COMPANYLIST:
        attempts += 1
        print(f"'{formated_user_input}' is not a company in the list ")

        if attempts > 1:
            attempts = 0
            print("Here is the list of companies.")

            for company in COMPANYLIST:
                print(f"{company }, " ,end="")

        get_user_company_name()




def get_input():
    """
    #### Gets hours and rate for storing the variables
    """
    hours : float = 0
    rate : float = 0
    while True:
        try: # Try getting user input as floats

            hours = float(input("Enter the hours worked: "))
            rate = float(input("Enter the rate : "))
            return hours, rate # Return both hours and rate to be stored
        except Exception as e: # If input is not a numerical value it will throw an exception
            print("Enter a valid number value.")




def compute_pay(hours, rate) -> tuple:
    """ 
     #### This function returns the 
     #####  pay_total,  hours_overtime,  hours,  overtime_pay
     
    """
    if hours > 40:
        hours_regular = 40
        hours_overtime = hours - 40
        OVERTIME_RATE = rate * 1.5
        overtime_pay = hours_overtime * OVERTIME_RATE
        regular_pay = hours_regular * rate
        pay_total = regular_pay + overtime_pay
        pay_total = round(pay_total,2)
    else:
        pay_total = hours * rate
        pay_total = round(pay_total,2)
    return pay_total # Return the pay results




def print_output(pay,company_name,hours,rate) -> None:
    """ Display a message to user of total pay"""
    global document_numbers
    document_number = randint(1000,2000)
    if document_number in document_numbers:
        document_number = randint(1000,2000)
    if document_number not in document_numbers:
        document_numbers.append(document_number)
        print(f"""          
        Company : {company_name}
        ------------------------------
        hours : {hours}
        rate  : {rate}
        
        The total pay is ${pay:.2f}
        ------------------------------
        Document #{document_number}
""")
    



def payProcess():
    '''
      This function is to process all other functions to get inputs,
      calculate and print the pay stub
    '''
    company_name = get_user_company_name()
    hours,rate = get_input()
    pay = compute_pay(hours,rate)
    print_output(pay,company_name,hours,rate)




def main():
    while True:
        payProcess()




if __name__ == "__main__":
    main()


"""
Output

Enter Company Name : w
'W' is not a company in the list 

Enter Company Name : tree
'Tree' is not a company in the list 
Here is the list of companies.
Apple, Microsoft, Google, Amazon, Uber, Facebook, 
Enter Company Name : uber
Enter the hours worked: 40
Enter the rate : 1

        Company : None
        ------------------------------
        hours : 40.0
        rate  : 1.0
        
        The total pay is $40.00
        ------------------------------
        Document #1779


Enter Company Name : company
'Company' is not a company in the list 

Enter Company Name : facebook
Enter the hours worked: 80
Enter the rate : 2

        Company : None
        ------------------------------
        hours : 80.0
        rate  : 2.0
        
        The total pay is $200.00      
        ------------------------------
        Document #1479
"""