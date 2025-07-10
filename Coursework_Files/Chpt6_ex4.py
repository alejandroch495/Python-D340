# Alejandro Chavez
# Chapter 6 extra credit
# Medals table sort
def main():
    listMedals("winners")
    listMedals("lose")
    listMedals("all")
    listMedals("gold")
    listMedals("silver")
    listMedals("bronze")


country_medals = {
                "Russia" : [0,1,2],
                "Canada" : [1,0,1],
                "France" : [1,0,1],
                "Japan" : [3,0,0],
                "Brazil" : [0,0,0],
                "Germany" : [0,1,1],
                "Italy" : [1,0,0],
                "South Korea" : [0,0,0],
                "Mexico" : [0,0,0],
                "China" : [1,3,0],
                "India" : [1,5,9],
                "United States" : [1,0,0]
                  }


def listMedals(medal_type):
    """ This displays the winners of the type that is entered.
    ### Medal types: 
    ##### all, winners, lose, gold, silver, and bronze"""
    medalCount,goldCount,silverCount,bronzeCount = 0,0,0,0
    
    
    if medal_type == 'all':
        print("\n\n These are all that participated.")
        print("|"+"Country".ljust(20)+"|"+"Gold".center(10)+"|"+"Silver".center(10)+"|"+"Bronze".center(10)+"|")
        
        for country in country_medals: # loop through dictionary names
            print(f'\n|{country.ljust(20)}|',end="") # print name

            # Get medals and save 
            goldCount += country_medals[country][0]
            silverCount += country_medals[country][1]
            bronzeCount += country_medals[country][2]
            for medals in country_medals[country]: # loop through the medals of the contry by name
                print(f'{str(medals).center(10)}|',end="") # print medals 
                medalCount += medals
        # Print total of medals and the amount of each medal(s)        
        print("\n|"+ f'Total medals are {medalCount}'.center(20) +"|"+ f'gold:{goldCount}'.center(10) +"|"+ f'silver:{silverCount}'.center(10) +"|"+ f'bronze:{bronzeCount}'.center(10)+"|")


    if medal_type == 'winners':
        print("\n\n These are all that participated and got a medal.")
        print("|"+"Country".ljust(20)+"|"+"Gold".center(10)+"|"+"Silver".center(10)+"|"+"Bronze".center(10)+"|")
        
        for country in country_medals:
            if sum(country_medals[country])>0: # If country got a medal, print the country and its medals
                print(f'\n|{country.ljust(20)}|',end="")

                # Get medals and save 
                goldCount += country_medals[country][0]
                silverCount += country_medals[country][1]
                bronzeCount += country_medals[country][2]
            
            for medals in country_medals[country]:
                if sum(country_medals[country])>0: # If country got a medal, print the country and its medals
                    print(f'{str(medals).center(10)}|',end="")
        # Print total of medals and the amount of each medal(s)            
        print("\n|"+ f'Total medals are {medalCount}'.center(20) +"|"+ f'gold:{goldCount}'.center(10) +"|"+ f'silver:{silverCount}'.center(10) +"|"+ f'bronze:{bronzeCount}'.center(10)+"|")

    if medal_type == 'lose':
        print("\n\n These are all that participated and got no medal.")
        print("|"+"Country".ljust(20)+"|"+"Gold".center(10)+"|"+"Silver".center(10)+"|"+"Bronze".center(10)+"|")
        
        for country in country_medals:
            if sum(country_medals[country])==0:# if country didn't get a medal. 
                print(f'\n|{country.ljust(20)}|',end="")

                # Get medals and save 
                goldCount += country_medals[country][0]
                silverCount += country_medals[country][1]
                bronzeCount += country_medals[country][2]
            for medals in country_medals[country]:
                if sum(country_medals[country])==0:# if country didn't get a medal.
                    print(f'{str(medals).center(10)}|',end="")
        # Print total of medals and the amount of each medal(s)            
        print("\n|"+ f'Total medals are {medalCount}'.center(20) +"|"+ f'gold:{goldCount}'.center(10) +"|"+ f'silver:{silverCount}'.center(10) +"|"+ f'bronze:{bronzeCount}'.center(10)+"|")

    if medal_type == 'gold':
        print("\n\n These are all that participated and got a gold medal.")
        print("|"+"Country".ljust(20)+"|"+"*Gold*".center(10)+"|"+"Silver".center(10)+"|"+"Bronze".center(10)+"|")
        
        for country in country_medals:
            if country_medals[country][0]>0: # If country got Gold medal, print
                print(f'\n|{country.ljust(20)}|',end="")

                # Get medals and save 
                goldCount += country_medals[country][0]
                silverCount += country_medals[country][1]
                bronzeCount += country_medals[country][2]
            for medals in country_medals[country]:
                if country_medals[country][0]>0: # If country got Gold medal, print
                    print(f'{str(medals).center(10)}|',end="")
        # Print total of medals and the amount of each medal(s)            
        print("\n|"+ f'Total medals are {medalCount}'.center(20) +"|"+ f'gold:{goldCount}'.center(10) +"|"+ f'silver:{silverCount}'.center(10) +"|"+ f'bronze:{bronzeCount}'.center(10)+"|")

    if medal_type == 'silver':
        print("\n\n These are all that participated and got a silver medal.")
        print("|"+"Country".ljust(20)+"|"+"Gold".center(10)+"|"+"*Silver*".center(10)+"|"+"Bronze".center(10)+"|")
        
        for country in country_medals:
            if country_medals[country][1]>0:# If country got silver medal, print
                print(f'\n|{country.ljust(20)}|',end="")

                # Get medals and save 
                goldCount += country_medals[country][0]
                silverCount += country_medals[country][1]
                bronzeCount += country_medals[country][2]
            for medals in country_medals[country]:
                if country_medals[country][1]>0:# If country got silver medal, print
                    print(f'{str(medals).center(10)}|',end="")
        # Print total of medals and the amount of each medal(s)            
        print("\n|"+ f'Total medals are {medalCount}'.center(20) +"|"+ f'gold:{goldCount}'.center(10) +"|"+ f'silver:{silverCount}'.center(10) +"|"+ f'bronze:{bronzeCount}'.center(10)+"|")

    if medal_type == 'bronze':
        print("\n\n These are all that participated and got a bronze medal.")
        print("|"+"Country".ljust(20)+"|"+"Gold".center(10)+"|"+"Silver".center(10)+"|"+"*Bronze*".center(10)+"|")
        
        for country in country_medals:
            if country_medals[country][2]>0:# If country got bronze medal, print
                print(f'\n|{country.ljust(20)}|',end="")

                # Get medals and save 
                goldCount += country_medals[country][0]
                silverCount += country_medals[country][1]
                bronzeCount += country_medals[country][2]
            for medals in country_medals[country]:
                if country_medals[country][2]>0:# If country got bronze medal, print
                    print(f'{str(medals).center(10)}|',end="")
        # Print total of medals and the amount of each medal(s)            
        print("\n|"+ f'Total medals are {medalCount}'.center(20) +"|"+ f'gold:{goldCount}'.center(10) +"|"+ f'silver:{silverCount}'.center(10) +"|"+ f'bronze:{bronzeCount}'.center(10)+"|")


if __name__ == "__main__":
    main()


"""
Output

 These are all that participated.
|Country             |   Gold   |  Silver  |  Bronze  |

|Russia              |    0     |    1     |    2     |
|Canada              |    1     |    0     |    1     |
|France              |    1     |    0     |    1     |
|Japan               |    3     |    0     |    0     |
|Brazil              |    0     |    0     |    0     |
|Germany             |    0     |    1     |    1     |
|Italy               |    1     |    0     |    0     |
|South Korea         |    0     |    0     |    0     |
|Mexico              |    0     |    0     |    0     |
|China               |    1     |    3     |    0     |
|India               |    1     |    5     |    9     |
|United States       |    1     |    0     |    0     |

 These are all that participated and got a medal.
|Country             |   Gold   |  Silver  |  Bronze  |

|Russia              |    0     |    1     |    2     |
|Canada              |    1     |    0     |    1     |
|France              |    1     |    0     |    1     |
|Japan               |    3     |    0     |    0     |
|Germany             |    0     |    1     |    1     |
|Italy               |    1     |    0     |    0     |
|China               |    1     |    3     |    0     |
|India               |    1     |    5     |    9     |
|United States       |    1     |    0     |    0     |

 These are all that participated and got no medal.
|Country             |   Gold   |  Silver  |  Bronze  |

|Brazil              |    0     |    0     |    0     |
|South Korea         |    0     |    0     |    0     |
|Mexico              |    0     |    0     |    0     |

 These are all that participated and got a gold medal.
|Country             |  *Gold*  |  Silver  |  Bronze  |

|Canada              |    1     |    0     |    1     |
|France              |    1     |    0     |    1     |
|Japan               |    3     |    0     |    0     |
|Italy               |    1     |    0     |    0     |
|China               |    1     |    3     |    0     |
|India               |    1     |    5     |    9     |
|United States       |    1     |    0     |    0     |
 These are all that participated and got a silver medal.
|Country             |   Gold   | *Silver* |  Bronze  |
|Russia              |    0     |    1     |    2     |
|China               |    1     |    3     |    0     |
|India               |    1     |    5     |    9     |

 These are all that participated and got a bronze medal.
|Country             |   Gold   |  Silver  | *Bronze* |

|Russia              |    0     |    1     |    2     |
|Canada              |    1     |    0     |    1     |
|France              |    1     |    0     |    1     |
|Germany             |    0     |    1     |    1     |
|India               |    1     |    5     |    9     |
"""