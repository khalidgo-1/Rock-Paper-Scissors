from attech import *
import random 

# 1= Paper ,2=Rock , 3= Scissors 
print(starting)
print(options)
 

while UScore <= 10 or ComScore <= 10:
    choice = input("choose form (Rock Paper Scissors) :")  
    choice.lower()
    
    for n in range(20):
        guess = random.randint(1,3)
        
    if choice == 'paper' :
        a = comp_chose(guess)
        print(f"You chose {choice}, The computer chose {a} ")
        
        if guess == 1 :
            # in this case guess = paper
            print(f"Drew !, your score is ({UScore}), computer's score is ({ComScore})\n")    
        elif guess == 2:
            # in this case guess = rock
            UScore += 1
            print(f"you scored point , your score is ({UScore}), computer's score is ({ComScore})\n")
        else:
            # in this case guess = scissors
            ComScore += 1
            print(f"computer scored point, your score is ({UScore}), computer's score is ({ComScore})\n")     
    elif choice == 'rock' :
        a = comp_chose(guess)
        print(f"You chose {choice}, The computer chose {a} ")

        if guess == 1 :
            # in this case guess = paper
            ComScore += 1
            print(f"computer scored point, your score is ({UScore}), computer's score is ({ComScore})\n")    
        elif guess == 2:
            # in this case guess = rock
            print(f"Drew !, your score is ({UScore}), computer's score is ({ComScore})\n") 

        else:
            # in this case guess = scissors
            UScore += 1
            print(f"you scored point , your score is ({UScore}), computer's score is ({ComScore})\n")       
    elif choice == 'scissors':
        a = comp_chose(guess)
        print(f"You chose {choice}, The computer chose {a} ")
        
        if guess == 1 :
            # in this case guess = paper
            UScore += 1
            print(f"you scored point , your score is ({UScore}), computer's score is ({ComScore})\n")
            
        elif guess == 2:
            # in this case guess = rock
            ComScore += 1
            print(f"computer scored point, your score is ({UScore}), computer's score is ({ComScore})\n")
            
        else:
            # in this case guess = scissors
            print(f"Drew !, your score is ({UScore}), computer's score is ({ComScore})\n") 
    elif choice == 'q':
        input('\nprocess is finished with code 0')
        exit()         
    else:
        print("your choice is not found , try again!")
        break
    if UScore == 10 :
        print(WinSign)
        input('\nprocess is finished with code 0')
        exit()
    elif ComScore == 10 :
        print(loseSign)
        input('\nprocess is finished with code 0')
        exit()

