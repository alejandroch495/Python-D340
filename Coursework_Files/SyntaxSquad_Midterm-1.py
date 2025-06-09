# Syntax Squad - Georgy Demyaneko, Himani Gupta, Jessica Toy, Alejandro Chavez, Sofia Iorgulescu, Khadijah Abdalla
# Midterm part 1
# The Grill - Customer ordering program


def main():
    display_menu()
    orders, status = get_orders()
    if sum(orders) != 0:
        subtotal,tax,total,status_str = compute_bill(orders,status)
        print_receipt(orders,status,subtotal,tax,total,status_str)
    else:
        print("Thank you! Hope to see you again!")
    

    
#-----------Function----------Split------------------------------------------------------------------------------   
     
#Display menu
def display_menu() -> str:
    """Displays a menu to user showing options, burger, and price to the user."""
    print(""" 
                    ___________________________
             ___.-=|De Anza grill - Burger Club|=-.___
            /______ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞ ͞  ______\\
           |_opt_|_____.-=[Burgers]=-._____|.-=Price=-.|
           |  1  |  De Anza Hamburger      |    $5.25  |
           |  2  |  The Western Burger     |    $5.95  |
           |  3  |  Bacon Cheese Burger    |    $5.75  |
           |  4  |  Don Cali Burger        |    $5.95  |
           |  5  |  Mushroom Swiss Burger  |    $5.95  |
           |_____|_________________________|___________|
           |6.   |  Exit Menu Or finalize order        |
            \\_________________________________________/

          """)
    return "Done"
    
#-----------Function----------Split------------------------------------------------------------------------------   
    
# Get orders
def staff_or_student() -> int: 
    
    """
    Asks user if they are 'staff' or 'student'. Returns an int value. 0 for student | 1 for staff.
    
    Returns:
         student:
        returns 0 if the users types 'student'
            
        staff:
        returns 1 if the users types 'staff'
    """
    
    get_input = input(" Are you 'staff' or 'student'. Type in response below \n staff or student? "  ).strip()
    try:
        if get_input.lower() == "staff":
            return 1
        elif get_input.lower() == "student":
            return 0
        else:
            print( "\nnot a valid input. Type 'staff' if you are a staff member or 'student' for a registered student. \n")
            return -1
    except Exception as e:
        print(e) 
        
    
#-----------Function----------Split------------------------------------------------------------------------------   

        
def get_orders():
    
    """
    Used to get the users selection of burger(s) and the quantities for each.
    
    Returns:
        choices : list :
            The 'choices' is a list of the 
            quantities stored corresponding to
            what the possible selections are.
    """
    
    SELECTION_OFFSET : int = -1 # Used to offset user selection to match the range within a list. 
    choices : list = [0,0,0,0,0]
    is_running : bool = True
    selection = None
    
    while is_running:
        try:
      
            if selection is None:
                selection = input("Please enter an option from above. 1 - 6\n  Option : ").strip()
                selection = int(selection)
            
            elif selection == 6: # exits loop
                break
                
            elif 1 <= selection <= 5: # If user enters valid number value
                quantity = input("Enter quantity : ").strip() # Get quantity
                if not quantity.isdigit() or int(quantity)<0:# If quantity value not positive and a whole number
                    print("enter a valid positive quantity") 
                else: # Add quantity for the selected choice
                    quantity = int(quantity)
                    choices[selection + SELECTION_OFFSET] = choices[selection + SELECTION_OFFSET] + quantity
                    selection = None
            else:
                selection = None
                
        except:
            print("Invalid option. Please enter a valid number from 1 - 6\n")
            selection = None # Reset selection or infinite loop is created
    while True:
        if sum(choices) !=0:
            status = -1
            if status < 0:
                status = staff_or_student()
            if status >= 0:
                break
        else:
            return choices, 0
        
    return choices, status


    
#-----------Function----------Split------------------------------------------------------------------------------   

        
def compute_bill(choices : list, status : int) -> tuple[float, float, float, str]:
    """
    
    parameters:
        choices: This is the list containing the quantities ordered
        status: Contains the int value. '0' == student '1' == staff
    
    returns:
        subtotal: price before tax -> float
        tax_out: tax of the subtotal -> float
        total: total price -> float"""
    FOOD_PRICES : list[float] = [5.25,5.95,5.75,5.95,5.95,5.95]
    TAX_TYPE : list[float] = [0.00,0.09]
    STATUS_STR : list[str] = ["Student","Staff"]
    tax : float = 0
    subtotal : float = 0
    total : float = 0

    #sets tax via input of param 'status'
    tax = TAX_TYPE[status]
    
    #sets string value for status to staff or student
    status_out = STATUS_STR[status]

    #calculates subtotal
    for counter in range(5):
        subtotal += FOOD_PRICES[counter] * choices[counter]
    #calculates tax total
    tax_out = round(subtotal * tax,2)
    #calculates total
    total = round(subtotal + tax_out,2)
    return subtotal,tax_out,total,status_out
    
    
#-----------Function----------Split------------------------------------------------------------------------------   
    
def print_receipt(  choices:list[int],  status:str,  subtotal:float,  tax:float,  total:float, status_out:str) -> None:
    FOOD_PRICES : list[float] = [5.25,5.95,5.75,5.95,5.95,5.95]
    BURGERS : list[str] =["De Anza Hamburger    ","The Western Burger   ","Bacon Cheese Burger  ","Don Cali Burger      ","Mushroom Swiss Burger"] 
    
    quantity:int = 0 # Amount ordered for specific burger
    burger_selection:str = "" # Burger name
    burger_price: float = 0 # Price of burger
    receipt_main_info: str = r"""
    
          
            |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
            |                                         |
            |              De Anza grill              |
            |               Burger Club               |
            |                                         |
            |              Cupertino, CA              |
            |     21250 Stevens Creek Blvd. 95014     |
            |                                         |
            |       In Campus Center Food Court       |
            |               Hours open:               |
            |            Monday - Thursday            |
            |           7:00 a.m - 3:30 p.m           |
            |       ---------------------------       |
            |                                         |
            |              Your Order(s)              |
            |       ---------------------------       |"""

    receipt_end_info: str = r"""            |       ---------------------------       |
            |                                         |
            |    Thank you! Hope to see you again!    |
            |                                         |
            |                  ________               |
            |                 /        \              |
            |                ~~~~~~~~~~~~             |
            |                ------------             |
            |                ############             |
            |                 \________/              |
            |                                         |
             \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|          
          """
    
    # "printing" of receipt is started
    print(receipt_main_info)
    for i in range(5): # Cycles/Iterates through each choices using 'i' as a counter 
        if choices[i] > 0:
            """
            Variables ending in '_spacer' and '_len' are used to keep the right distance 
            for the end of the paper based on the length of the original variables. 
            
            """
            quantity_spacer:str = " " # Default space
            price_spacer:str = "     "# Default space
            
            quantity = choices[i] # Quantity of burger at the position of 'i'
            quantity_len = len(str(quantity))
            
            if quantity_len > 1: # If the quantity ordered has more than length of 1 it will remove the spacer
                quantity_spacer = ""
                
            burger_price = round(choices[i] * FOOD_PRICES[i],2) # calculates the burger price for the current item 'i' each loop
            burger_price_str :str  = f"{burger_price:.2f}" # Converts it to string format to count length of string easier
            burger_price_len =len(burger_price_str) # Get length 

            if burger_price_len == 4:
                price_spacer = "     "
            if burger_price_len == 5:
                price_spacer = "    "
            if burger_price_len == 6:
                price_spacer = "   "
                
                
            burger_selection = BURGERS[i] # Get name of current burger
        
            print((" " * 12) + f"|   x{quantity}{quantity_spacer} {burger_selection}   ${burger_price_str}{price_spacer}|")
            # Line above prints the burgers quantity, name, and price
    
    """
    Variables ending in '_len' and '_spacer' are user to calculate distance from end of paper
    """
    
    subtotal_str: str = f"subtotal = ${subtotal :.2f}"
    tax_str: str = f"tax      = ${tax:.2f}"
    total_str: str = f"total    = ${total :.2f}"
    status_out = f"status   = {status_out}"
    
    subtotal_len = len(subtotal_str)
    tax_len = len(tax_str)
    total_len = len(total_str)
    status_out_len = len(status_out)
    
    subtotal_spacer = 21 - subtotal_len
    tax_spacer = 21 - tax_len
    total_spacer = 21 - total_len
    status_out_spacer = 21 - status_out_len
    
    print(f"""            |       ---------------------------       |
            |                    {status_out}{" " * status_out_spacer}|
            |                    {subtotal_str}{" " * subtotal_spacer}|
            |                    {tax_str}{" " * tax_spacer}|
            |                    {total_str}{" " * total_spacer}|""")
    print(receipt_end_info)
          
        

if __name__ == "__main__":
    main()
    
r"""
output

        Positive output

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


Please enter an option from above. 1 - 6
  Option : 1
Enter quantity : 1
Please enter an option from above. 1 - 6
  Option : 2
Enter quantity : 2
Please enter an option from above. 1 - 6
  Option : 3
Enter quantity : 3
Please enter an option from above. 1 - 6
  Option : 4
Enter quantity : 4
Please enter an option from above. 1 - 6
  Option : 5
Enter quantity : 15
Please enter an option from above. 1 - 6
  Option : 6
 Are you 'staff' or 'student'. Type in response below 
 staff or student? staff

    

            |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ 
            |                                         |
            |              De Anza grill              |
            |               Burger Club               |
            |                                         |
            |              Cupertino, CA              |
            |     21250 Stevens Creek Blvd. 95014     |
            |                                         |
            |       In Campus Center Food Court       |
            |               Hours open:               |
            |            Monday - Thursday            |
            |           7:00 a.m - 3:30 p.m           |
            |       ---------------------------       |
            |                                         |
            |              Your Order(s)              |
            |       ---------------------------       |
            |   x1  De Anza Hamburger       $5.25     |
            |   x2  The Western Burger      $11.90    |
            |   x3  Bacon Cheese Burger     $17.25    |
            |   x4  Don Cali Burger         $23.80    |
            |   x15 Mushroom Swiss Burger   $89.25    |
            |       ---------------------------       |
            |                    Status   = Staff     |
            |                    subtotal = $147.45   |
            |                    tax      = $13.27    |
            |                    total    = $160.72   |
            |       ---------------------------       |
            |                                         |
            |    Thank you! Hope to see you again!    |
            |                                         |
            |                  ________               |
            |                 /        \              |
            |                ~~~~~~~~~~~~             |
            |                ------------             |
            |                ############             |
            |                 \________/              |
            |                                         |
             \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|

        Exit output

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


Please enter an option from above. 1 - 6
  Option : 6
Thank you! Hope to see you again!


        Negative output

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


Please enter an option from above. 1 - 6
  Option : -1
Please enter an option from above. 1 - 6
  Option : 11
Please enter an option from above. 1 - 6
  Option : a
Invalid option. Please enter a valid number from 1 - 6

Please enter an option from above. 1 - 6
  Option : 1
Enter quantity : -1
enter a valid positive quantity
Enter quantity : a
enter a valid positive quantity
Enter quantity : 10
Please enter an option from above. 1 - 6
  Option : 6
 Are you 'staff' or 'student'. Type in response below 
 staff or student? asfeeawef

not a valid input. Type 'staff' if you are a staff member or 'student' for a registered student. 

 Are you 'staff' or 'student'. Type in response below 
 staff or student? 12

not a valid input. Type 'staff' if you are a staff member or 'student' for a registered student. 

 Are you 'staff' or 'student'. Type in response below 
 staff or student? student

    

            |\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ 
            |                                         |
            |              De Anza grill              |
            |               Burger Club               |
            |                                         |
            |              Cupertino, CA              |
            |     21250 Stevens Creek Blvd. 95014     |
            |                                         |
            |       In Campus Center Food Court       |
            |               Hours open:               |
            |            Monday - Thursday            |
            |           7:00 a.m - 3:30 p.m           |
            |       ---------------------------       |
            |                                         |
            |              Your Order(s)              |
            |       ---------------------------       |
            |   x10 De Anza Hamburger       $52.50    |
            |       ---------------------------       |
            |                    Status   = Student   |
            |                    subtotal = $52.50    |
            |                    tax      = $0.00     |
            |                    total    = $52.50    |
            |       ---------------------------       |
            |                                         |
            |    Thank you! Hope to see you again!    |
            |                                         |
            |                  ________               |
            |                 /        \              |
            |                ~~~~~~~~~~~~             |
            |                ------------             |
            |                ############             |
            |                 \________/              |
            |                                         |
             \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\|


"""