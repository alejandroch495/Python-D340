# Alejandro Chavez
# Chapter 4 exercise 1
# loop until user enters positive number
"""
Assignment requirements
-----------------------
# Ask the user to enter a number greater that zero. 
# Show an error if they entered a negative number
# keep asking the user to enter a positive number
# use a "while" loop
#-----------------------
"""

is_running = True # always true statment

while is_running: #is_running = True
    try:
        user_input = int(input("\nEnter a positive number : ")) # Get user input and convery into 'int' type
        if user_input > 0: # Check if user input is greater than 0
            print("\nThank you.\nDone! \nYou entered : ", user_input) # Give user feedback the program is done.
            is_running = False # Exit while loop by setting is_running to False
        else:
            print("Value is not a positive value!")
    except:
        print("\nError, Please enter a valid numeric value ")

        """
        output 'Negative value'

            Enter a positive number : -5
            Value is not a positive value!

        output 'Positive value'

            Enter a positive number : test

            Error, Please enter a valid numeric value

        ouput 'non-numerical value'
            Enter a positive number : 44

            Thank you.
            Done!
            You entered :  44
        """