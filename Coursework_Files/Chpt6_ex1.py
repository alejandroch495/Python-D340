# Alejandro Chavez
# Chapter 6 Exercise 1
# Friend list
def name(list):
    return list
friendList2017 : list[str] = ["Jim","Bobby","Joe","Brandon"]
friendList2018 : list[str] = ["Timmy","Larry","Guapo","Rico","John"]
is_running : bool = True
user_input : str = ""
name = None
found_friend : bool = False
while is_running:

    if name == None: # ask for friends name if one wasn't previously given
        user_input = input("Enter friends name: ").strip()

    #see if in any of the lists
    if user_input in friendList2017 and name == None:
        print(f" friend {user_input} meet in 2017")
        found_friend = True

    if user_input in friendList2018 and name == None:
        print(f" friend {user_input} meet in 2018")        
        found_friend = True

    # name not in lists. save for future reference
    if name == None and not found_friend:
        name = user_input

        #get year met
        user_input = input(f"What year did you meet {name}. \n Enter 2018 or 2017 : ")

    # if meet in 2017 or 2018 add to list corrisponding to input
    if user_input == "2017":
        print(name, "added to 2017")
        friendList2017.append(name)
        name = None
    elif user_input == "2018":
        print(name, "added to 2018")
        friendList2018.append(name)
        name = None

    #inform user a valid input must be entered
    elif found_friend != True and name != None:
        print(name)
        print("not a valid year.")
    print(friendList2017 + friendList2018)

    """
    Output:
Enter friends name: tim
What year did you meet tim. 
 Enter 2018 or 2017 : 2018  
tim added to 2018
['Jim', 'Bobby', 'Joe', 'Brandon', 'Timmy', 'Larry', 'Guapo', 'Rico', 'John', 'tim']
Enter friends name: Jim
 friend Jim meet in 2017
['Jim', 'Bobby', 'Joe', 'Brandon', 'Timmy', 'Larry', 'Guapo', 'Rico', 'John', 'tim']
Enter friends name: Bobby
 friend Bobby meet in 2017
['Jim', 'Bobby', 'Joe', 'Brandon', 'Timmy', 'Larry', 'Guapo', 'Rico', 'John', 'tim']
Enter friends name: Larry
 friend Larry meet in 2018
['Jim', 'Bobby', 'Joe', 'Brandon', 'Timmy', 'Larry', 'Guapo', 'Rico', 'John', 'tim']
Enter friends name:
"""