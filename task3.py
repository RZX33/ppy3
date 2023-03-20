import random


def number_of_the_rounds():
    return int(input('Input number of rounds'))


possible_actions = ["rock", "paper", "scissors"]
gameChoice = input('Input choice (computer or hotseats)')
if gameChoice == 'computer':
    roundNumber = number_of_the_rounds()
    rounds = []
    for i in range(0, roundNumber):
        playerChoice = True
        playerMove = ''
        while playerChoice:
            playerMove = input('Input move')
            if playerMove in possible_actions:
                playerChoice = False
        computerMove = random.choice(possible_actions)
        print(computerMove)
        if computerMove == playerMove:
            rounds.append(0)
        elif (computerMove == possible_actions[0] and playerMove == possible_actions[1]) or (computerMove == possible_actions[1] and playerMove == possible_actions[2]) or (computerMove == possible_actions[2] and playerMove == possible_actions[0]):
            rounds.append(1)
        else:
            rounds.append(-1)
    pointSum = 0
    for i in range(0, len(rounds)):
        pointSum+=rounds[i]
        if rounds[i]==0:
            print('round ', i, ' - draw')
        elif rounds[i]==1:
            print('round ', i, ' - won')
        else:
            print('round ', i, ' - lost')
    if pointSum == 0:
        print('draw')
    elif pointSum == 1:
        print('won')
    else:
        print('lost')
elif gameChoice == 'hotseats':
    roundNumber = number_of_the_rounds()
    rounds = []
    playerChoice = 1

