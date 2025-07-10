# Alejandro Chavez
# Chapter 9 exercise 1
# Class pay system
from random import randint
class PayClass:
        COMPANYLIST : list[str] = ['Apple', 'Microsoft', 'Google','Amazon', 'Uber', 'Facebook']
        OVERTIME = 1.5
        name = ""
        REGULAR_HOURS_MAX = 40
        hours: float = 0
        rate : float = 0
        overtime_hours = 0
        payout: float = 0
        _document_numbers : list[int] = []
        company_name: str = ""
        
        
        def __init__(self, employee):
            self.name = employee
            print("The object", employee, "has been created!")
            self.get_user_company_name()
        
        
        def getInputs(self):
            while True:
                try: # Try getting user input as floats
                    self.hours = float(input("Enter the hours worked: "))
                    self.rate = float(input("Enter the rate : "))
                    if self.hours >= 0 and self.rate >= 0:
                        self.hours, self.rate # Return both hours and rate to be stored
                        self.calculatePay()
                        break
                    else: 
                        print(f'Enter positive values!')
                except Exception as e: # If input is not a numerical value it will throw an exception
                    print("Enter a valid number value.")
        
        
        def calculatePay(self):
            if self.hours > 40:
                self.overtime_hours = self.hours - 40
                self.hours = self.REGULAR_HOURS_MAX
            self.payout = (self.overtime_hours * self.rate * self.OVERTIME) + (self.hours * self.rate)
            self.print_output()
        
        
        # This function formats input so the first letter is always capitolized
        def format_input(self, input):
            '''##### Turns input into a formated string that always has the first letter capitolized.
            ### Example : "apPle" -> "Apple"'''
            if input != "":
                ending_letters = ""
                first_letter, *remaining_letters = input
                for i in remaining_letters:
                    ending_letters += i
                return_var = first_letter.capitalize() + ending_letters
                return return_var
            else: 
                return " "


        def get_user_company_name(self):
            '''### Saves users entered company name.
            If incorrect company name is entered twice it will output a list of options availible'''
            self._attempts = 0
            print()

            user_input = input('Enter Company Name : ').strip().lower()

            formated_user_input = self.format_input(user_input)

            if formated_user_input in self.COMPANYLIST:
                self.company_name = formated_user_input
            
            if formated_user_input not in self.COMPANYLIST:
                self._attempts += 1
                print(f"'{formated_user_input}' is not a company in the list ")

                if self._attempts > 1:
                    self._attempts = 0
                    print("Here is the list of companies.")

                    for company in self.COMPANYLIST:
                        print(f"{company }, " ,end="")

                self.get_user_company_name()


        def print_output(self) -> None:
            """ Display a message to user of total pay"""
            self._document_numbers
            self._document_number = randint(1000,2000)
            if self._document_number in self._document_numbers:
                self._document_number = randint(1000,2000)
            if self._document_number not in self._document_numbers:
                self._document_numbers.append(self._document_number)
                print(f"""          
                Company : {self.company_name}
                Employee : {self.name}
                ------------------------------
                hours : {self.hours:.2f}
                rate  : {self.rate:.2f}
                
                The regular pay is ${self.hours * self.rate:.2f}
                ------------------------------
                Overtime hours : {self.overtime_hours:.2f}
                Overtime rate  : {self.rate * self.OVERTIME:.2f}
                
                The overtime pay is ${self.overtime_hours * self.rate * self.OVERTIME:.2f}
                ------------------------------
                Total pay is ${self.payout:.2f}
                ------------------------------
                Document #{self._document_number}
        """)
 
 
pay1 = PayClass("Jimmy")
pay1.getInputs()
pay2 = PayClass("Jeniffer")
pay2.getInputs()


"""
Output
The object Jimmy has been created!

Enter Company Name : amazon
Enter the hours worked: 40
Enter the rate : 1

                Company : Amazon
                Employee : Jimmy
                ------------------------------
                hours : 40.00
                rate  : 1.00

                The regular pay is $40.00     
                ------------------------------
                Overtime hours : 0.00
                Overtime rate  : 1.50

                The overtime pay is $0.00     
                ------------------------------
                Total pay is $40.00
                ------------------------------
                Document #1925

The object Jeniffer has been created!

Enter Company Name : 80
'80' is not a company in the list 

Enter Company Name : uber
Enter the hours worked: 80
Enter the rate : 2

                Company : Uber
                Employee : Jeniffer
                ------------------------------
                hours : 40.00
                rate  : 2.00

                The regular pay is $80.00
                ------------------------------
                Overtime hours : 40.00
                Overtime rate  : 3.00

                The overtime pay is $120.00
                ------------------------------
                Total pay is $200.00
                ------------------------------
                Document #1733
"""