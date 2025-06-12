# Alejandro Chavez
# Chapter 6 exercise 2
# Names - using dictionaries

"""
-Create a dictionary of your friends that you met in 2017 and 2018. So, the keys are '2017' and '2018' and the values are the list of the friends. 
"""

friends_list: dict = {"2017" : ["Jim", "Darryl", "Jen","Bob", "Jill"], "2018" : ["Tim", "Jack", "Brandon", "Jessica", "Matthew", "Blake"]}
friend_found = False
def print_friends_list() -> None:
        for year in friends_list:
            print()
            print(f"Year : {year} \n  Friends : " ,end= " ")
            for friend in friends_list[year]:
                print(f" {friend}, ", end= "")    

print('Press enter to see friends list again. \n\nType name of friend to either see when you met them \nor would like to add them to the list')
print_friends_list()
def get_user_input():
    global friend_found
    print()
    # -Ask the user to enter the name of a friend.
    user_input = input('Enter a friends name : ').strip()


    #-Prints the friends' names in the dictionary 
    if user_input == "":
        print_friends_list()


    # 
    else:

        # -Then show that friend you met in what year, 2017 or 2018.
        for year in friends_list:
            if user_input in friends_list[year]:
                print(f'{user_input} met in {year}')
                friend_found = True
                break

        # -Ask the user to enter a new friend name to be added to the 2017 or 2018 lists (You need also to ask the user what year they want to add the friend's name).
        if friend_found == False:
            name = user_input
            user_input_year = input(f"{name} is not in the friends lists. Enter year {name} was met: ").strip()

            # -Then add the entered friend's name to the dictionary( to the value of the 2017 key or the value of the 2018 key)  
            if user_input_year in friends_list:
                friends_list[user_input_year].append(name)
                print_friends_list()
            else:
                friends_list[user_input_year] = [name,]
                print_friends_list()
    friend_found = False
    


def main():
    while True:
        get_user_input()
if __name__ == "__main__":
    main()


"""
        Output

Press enter to see friends list again. 

Type name of friend to either see when you met them 
or would like to add them to the list

Year : 2017 
  Friends :   Jim,  Darryl,  Jen,  Bob,  Jill, 
Year : 2018 
  Friends :   Tim,  Jack,  Brandon,  Jessica,  Matthew,  Blake, 
Enter a friends name : Jim
Jim met in 2017        

Enter a friends name : Tim
Tim met in 2018        

Enter a friends name : Job
Job is not in the friends lists. Enter year Job was met: 2017

Year : 2017
  Friends :   Jim,  Darryl,  Jen,  Bob,  Jill,  Job,
Year : 2018
  Friends :   Tim,  Jack,  Brandon,  Jessica,  Matthew,  Blake,
Enter a friends name : Trent
Trent is not in the friends lists. Enter year Trent was met: 2025

Year : 2017
  Friends :   Jim,  Darryl,  Jen,  Bob,  Jill,  Job,
Year : 2018
  Friends :   Tim,  Jack,  Brandon,  Jessica,  Matthew,  Blake,
Year : 2025
  Friends :   Trent,
Enter a friends name : Josh
Josh is not in the friends lists. Enter year Josh was met: 2025

Year : 2017
  Friends :   Jim,  Darryl,  Jen,  Bob,  Jill,  Job,
Year : 2018
  Friends :   Tim,  Jack,  Brandon,  Jessica,  Matthew,  Blake,
Year : 2025
  Friends :   Trent,  Josh,
"""