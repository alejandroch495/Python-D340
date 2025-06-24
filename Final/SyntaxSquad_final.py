# Syntax Squad - Georgy Demyaneko, Himani Gupta, Jessica Toy, Alejandro Chavez, Sofia Iorgulescu, Khadijah Abdalla
# Final part 1 
# The Grill - Customer ordering program - refactored for containing into classes
from time import time
from datetime import datetime
now_time = time()
date = datetime.fromtimestamp(now_time).strftime("%Y/%m/%d")
timeOfDay = datetime.fromtimestamp(now_time).strftime("%H:%M:%S")
print(date)


def main():
    customer : Order = Order()
    customer.get_user_input()
    customer.printReceipt()
    customer.saveToFile()   


class Order:
    """#### Used to create customer orders."""
    # Menu options and price
    menu_options = {"De Anza Hamburger" : 5.25, 
                "The Western Burger" : 5.95,
                "Bacon Cheese Burger" : 5.75,
                "Don Cali Burger" : 5.95,
                "Mushroom Swiss Burger" : 5.95}
    

    def __init__(self):
        """Creates a new order for a customer."""
        # Variables for billing
        self._subtotal = [] # Before tax
        self._total = 00.00 # After tax
        self._tax = 0.00 # Tax amount
        self._status = ''
        self._taxes = {"student" : 0.00, "staff" : 0.09}
        self.status_options = ["student", "staff"]
        
        # Variables for getting option selection and quantities from user input
        self._menu_items =[]
        self.orders = {
            "De Anza Hamburger" : 0, 
            "The Western Burger" : 0,
            "Bacon Cheese Burger" : 0,
            "Don Cali Burger" : 0,
            "Mushroom Swiss Burger" : 0
            }
        
        # This gets the menu items to get the right option input
        for item in self.orders:
            self._menu_items.append(item)



    def print_menu(self):
        """Displays a menu to user showing options, burger, and price to the user."""
        print(r""" 
                    ___________________________
             ___.-=|De Anza grill - Burger Club|=-.___
            /______ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞  ______\
           |_opt_|_____.-=[Burgers]=-._____|.-=Price=-.|
           |  1  |  De Anza Hamburger      |    $5.25  |
           |  2  |  The Western Burger     |    $5.95  |
           |  3  |  Bacon Cheese Burger    |    $5.75  |
           |  4  |  Don Cali Burger        |    $5.95  |
           |  5  |  Mushroom Swiss Burger  |    $5.95  |
           |_____|_________________________|___________|
           |6.   |  Exit Menu Or finalize order        |
            \_________________________________________/

          """)
        
    def getOrder(self):
        "Gets current order information."
        print(self.orders)
    
    def setOrder(self,option,quantity):
        "Sets/adds quantity for option selected"
        self.orders[option] = quantity
        



    def get_user_input(self):

        # Used as a toggle switch to go back and forth from getting option or quantity
        self._current_selection = -1
        # Display menu
        self.print_menu()

        # Begging loop from getting user input
        while True:
            # Get users option from menu
            if self._current_selection == -1:
                try:
                    user_input = int(input('Enter an option from the menu above by entering the number associated with that option.\nEnter number: ').strip())   
                    if user_input ==6:
                        break 
                    if user_input < 1 or user_input > 6:
                        print("\n\nPlease enter a valid option number 1 - 5 or 6 to quit/continue\n")
                    else:
                        self._current_selection = user_input 
                # Try getting valid option menu item
                except:
                    print("\n\nThe option you entered is not a valid numerical value.\nPlease enter a number from the menu\n\n") 
                # If user enters a value that cannot be turned into an int


            # Get users quantity of their option selected
            if self._current_selection != -1:
                try:
                    user_input = int(input("Enter the quantity you would like to order.\nQuantity: "))
                    if user_input == 0:
                        self._current_selection = -1
                    elif user_input > 0:
                        if self.orders[self._menu_items[self._current_selection-1]] == 0:
                            self.orders[self._menu_items[self._current_selection-1]] = user_input
                        else:
                            self.orders[self._menu_items[self._current_selection-1]] += user_input
                        self._current_selection = -1
                        
                    else:
                        print("\nPlease enter a POSITIVE numerical value.\n")
                # try getting user input for quantity amount
                except:
                    print("You entered a non-positive and non-numerical value\nPlease enter a valid numerical value.\n")
                # If user enters a value that cannot be turned into an int
            # if user has entered a valid option
        # This loops until user enters a valid status 
        while True:
            if self._status == '':
                self.staff_or_student()
            elif self._status == "student" or self._status == "staff" :
                # Once user inputs valid status: Computes bill
                self._computeBill()
                break

    def _computeBill(self):

        # Looks through the orders one item at a time
        for item in self.orders:
            # Saves items total cost based on quantity ordered
            subtotal_item = round(self.menu_options[item] * self.orders[item],2)
            # Adds items total to the list
            self._subtotal.append(subtotal_item)
        # Calculates tax
        self._tax = round(sum(self._subtotal) * self._taxes[self._status],2)
        # Calculates Total
        self._total = round(sum(self._subtotal) + self._tax,2)

    def staff_or_student(self):
        """
        Asks user if they are 'staff' or 'student'.
        """
        
        get_input = input(" Are you 'staff' or 'student'. Type in response below \n staff or student? "  ).strip()
        try:
            if get_input.lower() == "staff":
                self._status = self.status_options[1]
            elif get_input.lower() == "student":
                self._status = self.status_options[0]
            else:
                print( "\nnot a valid input. Type 'staff' if you are a staff member or 'student' for a registered student. \n")
                
        except Exception as e:
            print(e) 


    

    def printReceipt(self): 

        # Used for styling
        receipt_length = 43
        offset = 4
        
        # Used for visual output and writing output
        self._print_out_list =[]
        self._save_out_list = []

        # Adds important information about the restraunt. Includes the time and date of the order.
        receipt_main_info = rf"""

    
          
            |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
            |                                           |
            |              De Anza grill                |
            |               Burger Club                 |
            |                                           |
            |              Cupertino, CA                |
            |     21250 Stevens Creek Blvd. 95014       |
            |                                           |
            |       In Campus Center Food Court         |
            |               Hours open:                 |
            |            Monday - Thursday              |
            |           7:00 a.m - 3:30 p.m             |
            |       ---------------------------         |
            |{date.center(receipt_length)}|
            |{timeOfDay.center(receipt_length)}|
            |{"Your Order(s)".center(receipt_length)}|
            |       ---------------------------         |"""
        
        # Ending message to the customer on the receipt
        receipt_end_info = r"""            |       ---------------------------         |
            |                                           |
            |    Thank you! Hope to see you again!      |
            |                                           |
            |                  ________                 |
            |                 /        \                |
            |                ~~~~~~~~~~~~               |
            |                ------------               |
            |                ############               |
            |                 \________/                |
            |                                           |
             \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|          
          """
        
        # Adds main beginning information to the lists

        self._print_out_list.append(receipt_main_info)
        self._save_out_list.append(receipt_main_info)
        
        # Calculation gets the name, quantity, price, and total for the current burger found in orders
        # example :            |      De Anza Hamburger x 1 x 5.25 - 5.25  | 
        # This is then saved into the list containing the list of items to later output
        for item in self.orders:
            _subtotal_item = round(self.menu_options[item] * self.orders[item],2)
            if _subtotal_item > 0:
                item_print = str(f"{item.rjust(21)} x {self.orders[item]} x {self.menu_options[item]} - {_subtotal_item:.2f}")
                self._print_out_list.append(f"            |{item_print.center(receipt_length)}|")

        # Calculation gets the name, quantity, price, and total for the current burger found in orders
        # The difference between this one and the one above is that this one adds a '\n' to let the file writer know to to go the next line
        # example :            |      De Anza Hamburger x 1 x 5.25 - 5.25  | 
        # This is then saved into the list containing the list of items to later output
        for item in self.orders:
            _subtotal_item = round(self.menu_options[item] * self.orders[item],2)
            if _subtotal_item > 0:
                item_print = str(f"{item.rjust(21)} x {self.orders[item]} x {self.menu_options[item]} - {_subtotal_item:.2f}")
                self._save_out_list.append(f"\n            |{item_print.center(receipt_length)}|")
        
        # This adds the final billing information to the print out on the display output list
        self._print_out_list.append(f"""            |       ---------------------------         |
            |{("Status = " + self._status).rjust(receipt_length-offset)}    |
            |{("Subtotal = " + str(round(sum(self._subtotal),2))).rjust(receipt_length-offset)}    |
            |{("Tax = " + str(self._tax)).rjust(receipt_length-offset)}    |
            |{("Total = " + str(self._total)).rjust(receipt_length-offset)}    |""")
        # This adds the final billing information to the print out into the file output list
        self._save_out_list.append(f"""\n            |       ---------------------------         |
            |{("Status = " + self._status).rjust(receipt_length-offset)}    |
            |{("Subtotal = " + str(round(sum(self._subtotal),2))).rjust(receipt_length-offset)}    |
            |{("Tax = " + str(self._tax)).rjust(receipt_length-offset)}    |
            |{("Total = " + str(self._total)).rjust(receipt_length-offset)}    |""")
        
        # Attaches ending receipt information to the lists
        self._print_out_list.append(receipt_end_info)
        self._save_out_list.append("\n"+ receipt_end_info)

        # Prints all lines saved for the receipt
        for lines in self._print_out_list:
            print(lines)

        
    def saveToFile(self):
        file = open("printedBill.txt","w")
        for lines in self._save_out_list:
            file.write(lines)
        file.close()


if __name__ == "__main__":
    main()



"""
Inputs
positive outputs (option/quantites input)
1,1,2,2,3,3,4,4,5,5

negative outputs (option/quantites input)
-4,4,-1,-4141,40

exit (option/quantites input)
6

negative output(status input)
studetn,1

positive output(status input)
student


Output 

 
                    ___________________________
             ___.-=|De Anza grill - Burger Club|=-.___
            /______ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞  ______\
           |_opt_|_____.-=[Burgers]=-._____|.-=Price=-.|
           |  1  |  De Anza Hamburger      |    $5.25  |
           |  2  |  The Western Burger     |    $5.95  |
           |  3  |  Bacon Cheese Burger    |    $5.75  |
           |  4  |  Don Cali Burger        |    $5.95  |
           |  5  |  Mushroom Swiss Burger  |    $5.95  |
           |_____|_________________________|___________|
           |6.   |  Exit Menu Or finalize order        |
            \_________________________________________/


Enter an option from the menu above by entering the number associated with that option.
Enter number: 1
Enter the quantity you would like to order.
Quantity: 1
Enter an option from the menu above by entering the number associated with that option.
Enter number: 2
Enter the quantity you would like to order.
Quantity: 2
Enter an option from the menu above by entering the number associated with that option.
Enter number: 3
Enter the quantity you would like to order.
Quantity: 3
Enter an option from the menu above by entering the number associated with that option.
Enter number: 4
Enter the quantity you would like to order.
Quantity: 4
Enter an option from the menu above by entering the number associated with that option.
Enter number: 5
Enter the quantity you would like to order.
Quantity: 5
Enter an option from the menu above by entering the number associated with that option.
Enter number: -4


Please enter a valid option number 1 - 5 or 6 to quit/continue

Enter an option from the menu above by entering the number associated with that option.
Enter number: 4
Enter the quantity you would like to order.
Quantity: -1

Please enter a POSITIVE numerical value.

Enter the quantity you would like to order.
Quantity: -4141

Please enter a POSITIVE numerical value.

Enter the quantity you would like to order.
Quantity: 40
Enter an option from the menu above by entering the number associated with that option.
Enter number: 6
 Are you 'staff' or 'student'. Type in response below 
 staff or student? student




            |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
            |                                           |
            |              De Anza grill                |
            |               Burger Club                 |
            |                                           |
            |              Cupertino, CA                |
            |     21250 Stevens Creek Blvd. 95014       |
            |                                           |
            |       In Campus Center Food Court         |
            |               Hours open:                 |
            |            Monday - Thursday              |
            |           7:00 a.m - 3:30 p.m             |
            |       ---------------------------         |
            |                 2025/06/23                |
            |                  21:20:11                 |
            |               Your Order(s)               |
            |       ---------------------------         |
            |      De Anza Hamburger x 1 x 5.25 - 5.25  |
            |     The Western Burger x 2 x 5.95 - 11.90 |
            |    Bacon Cheese Burger x 3 x 5.75 - 17.25 |
            |       Don Cali Burger x 44 x 5.95 - 261.80|
            |  Mushroom Swiss Burger x 5 x 5.95 - 29.75 |
            |       ---------------------------         |
            |                       Status = student    |
            |                      Subtotal = 325.95    |
            |                              Tax = 0.0    |
            |                         Total = 325.95    |
            |       ---------------------------         |
            |                                           |
            |    Thank you! Hope to see you again!      |
            |                                           |
            |                  ________                 |
            |                 /        \                |
            |                ~~~~~~~~~~~~               |
            |                ------------               |
            |                ############               |
            |                 \________/                |
            |                                           |
             \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|"""