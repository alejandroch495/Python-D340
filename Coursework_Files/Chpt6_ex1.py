# Alejandro Chavez
# Chapter 6 exercises 1
# Friend list


friend_list_2017 : list[(str,int)] = [("Bob",2017),("Tim",2017),("Brandon",2017)]
friend_list_2018 : list[(str,int)] = [("Jeff",2018),("Brandon",2018),("Angel",2018)] 




def display_friends() -> None:
    print("| Name     | Year |")
    for i in friend_list_2017:
        
        name : str = i[0]
        year : int = i[1]
        name_spacer : int = 9 - len(name)
        print(f"| {name}{' ' * name_spacer}| {year:4.0f} |") 
    for i in friend_list_2018:
        
        name : str = i[0]
        year : int = i[1]
        name_spacer : int = 9 - len(name)
        print(f"| {name}{' ' * name_spacer}| {year:4.0f} |") 
display_friends()