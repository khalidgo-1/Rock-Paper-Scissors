
starting = "="*30+"\nRock Paper Scissors\n"+"="*30
options = ">"*3+'Write "q" to quit from the game'+"<"*3 


commove = ""

UScore = 0
ComScore = 0


game = 0

WinSign = "="*30+"\nYOU WON !, Your score reached (10)\n"+"="*30
loseSign = "="*30+"\nYOU LOSE!, computer score reached (10)\n"+"="*30



def comp_chose(guess):
    from Game import guess
    if guess == 1:
        commove = 'paper'
    elif guess == 2:
        commove = 'rock'
    elif guess == 3:
        commove = 'scissors'
    return commove
        