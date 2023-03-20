import random
import getpass


def number_of_the_rounds():
    return int(input('Input number of rounds'))


possible_actions = ["rock", "paper", "scissors"]
gameChoice = input('Input choice (computer or hotseats)')
if gameChoice == 'computer':
    roundNumber = number_of_the_rounds()
    rounds = []
    for i in range(0, roundNumber):
        player1Choice = True
        player1Move = ''
        while player1Choice:
            player1Move = input('Input move')
            if player1Move in possible_actions:
                player1Choice = False
        player2Move = random.choice(possible_actions)
        print(player2Move)
        if player2Move == player1Move:
            rounds.append(0)
        elif (player2Move == possible_actions[0] and player1Move == possible_actions[1]) or (
                player2Move == possible_actions[1] and player1Move == possible_actions[2]) or (
                player2Move == possible_actions[2] and player1Move == possible_actions[0]):
            rounds.append(1)
        else:
            rounds.append(-1)
    pointSum = 0
    for i in range(0, len(rounds)):
        pointSum += rounds[i]
        if rounds[i] == 0:
            print('round ', i, ' - draw')
        elif rounds[i] == 1:
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
    player1 = input('Input player 1 name')
    player2 = input('Input player 2 name')
    pointSum = 0
    for i in range(0, roundNumber):
        player1Choice = True
        player1Move = ''
        while player1Choice:
            player1Move = getpass.getpass('Input move '+player1)
            if player1Move in possible_actions:
                player1Choice = False
        player2Choice = True
        player2Move = ''
        while player2Choice:
            player2Move = getpass.getpass('Input move '+player2)
            if player2Move in possible_actions:
                player2Choice = False
        print(player1Move+' '+player2Move)
        if player2Move == player1Move:
            rounds.append(0)
        elif (player2Move == possible_actions[0] and player1Move == possible_actions[1]) or (
                player2Move == possible_actions[1] and player1Move == possible_actions[2]) or (
                player2Move == possible_actions[2] and player1Move == possible_actions[0]):
            rounds.append(1)
        else:
            rounds.append(-1)
    for i in range(0, len(rounds)):
        pointSum += rounds[i]
        if rounds[i] == 0:
            print('round ', i, ' - draw')
        elif rounds[i] == 1:
            print('round ', i, ' - won')
        else:
            print('round ', i, ' - lost')
    if pointSum == 0:
        print('draw')
    elif pointSum == 1:
        print('won')
    else:
        print('lost')
