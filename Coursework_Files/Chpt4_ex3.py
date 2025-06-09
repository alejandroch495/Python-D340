# Alejandro Chavez
# Chapter 4 exercise 3
# Domain / E-mail checker

# Function splits email into 3 seperate parts. User_id, domain_name, and top_level_domain
def splitEmail(user_input : str, DELIMITERS, email_split : list[str]) -> None:
    temp : str = '' 
    counter = 0
    for i in user_input:
                counter = counter + 1
                if i not in DELIMITERS:
                    temp = temp + i
                if i == '@' or i == '.' or counter == len(user_input):
                    email_split.append(temp)
                    temp = ''
                    
# Function checks to see if there the input has the DELIMITERS we have hard coded
# Returns True or False
def contains_DELIMITERS(user_input : str, DELIMITERS : list[str]) -> bool:
    for value in DELIMITERS:
        if value in user_input:
            return True
    return False
    
user_input : str = ""
is_running : bool = True
DELIMITERS : list[str] = ['@','.']
email_split: list[str] = []
while is_running:
    try:
        # prompt for email
        user_input = input("Enter E-mail: ")
        # Check valid email. Must contain '@' and '.'
        if contains_DELIMITERS(user_input, DELIMITERS):
            splitEmail(user_input, DELIMITERS, email_split)
            if len(email_split) < 4:
                print(f"Email : {user_input}\nDomain : {email_split[1]}")
                is_running = False
            else:
                print("Too many '@' or '.' characters entered")
                email_split.clear()
        else:
            print("Not a valid email address!")
        # Return domain
    except Exception as e:
        print(e)
    
"""
output

Enter E-mail: test@gmail.com
Email : test@gmail.com
Domain : gmail

Enter E-mail: joe@yahoo.com 
Email : joe@yahoo.com 
Domain : yahoo
"""