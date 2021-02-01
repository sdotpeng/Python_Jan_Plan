''' Top-down design '''

'''
Example adapted from Zelle
As you start working on more complex programs, it helps to have guiding principles to help
deal with what might seem to be a daunting task. One of the most useful principles is
called Top-down design

I think this is best understood by working through an entertaining example

Let's consider the scenario of making a program that simulates two players plaing a number of
games of the sport recquetball. I'm adapting this example from Zelle.
'''

'''
---- Basic rules of racquetball ----
* Game is similar to tennis and volleyball. Players hit a ball with a racquet back and forth
in a court
* To start the game, one of the players puts the ball into play -- this is called serving
* The players then alternate hitting the ball to keep it in play; this is a rally. The
rally ends when one of the players fails to hit a legal shot
* The player who misses the shot loses the rally
    * If the loser is the player who served, then no points are won or lost: the other
    player now serves the ball
    * If the server wins the rally, a point is awarded. Players can only score points
    if they are serving.
* The first player to reach 15 points wins the game
'''

'''
Problem: Let's say `Player A` plays `Player B` in a championship of `n` total games.
How many of the games would we expect `Player A` and `Player B` to win in the championship?

This will of course depend on how good the players are at winning points. Let's say that
`Player A` has a history of wining a point on their serve a proportion of time
`probA (number between 0 and 1)`. We also know that Player B has a history of winning a point
on their serve a proportion of time `probB`.
'''

'''
Pseudocode

Simulating the game might seem daunting, but let's break down the problem into high level
tasks that need to get done for us to write the program

Let's write the steps as comments in `main` function.
    1. We print an introduction to users, instructing them what program does.
    2. We ask the user to enter the probability that player A wins at a serve, another one
    that Player B wins at a serve, and then number of gmaes in the championship.
    3. Simulate `n` games of racquetball using `probA` and `probB`
    4. Output a written summary of the number of games won by each player
    5. Writing out an outline of steps we need to complete in a program in English rather
    than exact code is called pseudocode
    6. Programmers often write pseudo code in comments to plan out code to write in the future.
    7. I often use pseudocode in class examples to break down what tasks I need to follow
    when live coding.
'''

'''
    - The loser is the one who failed to hit ball back during the rally
    - If the loser was the one who served, no points won or lost, the other serves now.
    - If the server wins, that player gets a point

    - IMPORTANT: Game ends when one player gets 15 points.
'''

import random

def printInstructions():
    ''' Print instructions on the screen '''
    print('This program simulates a game of racquetball between two',
    'players called A and B. The abilities of each play is',
    'indicated by a probability (number between 0 and 1) that',
    'the player wins the point when serving. Player A always',
    'has the first serve.')

def getUserInput():
    ''' Get user input from the terminal '''
    probWinA = float(input('Please enter the prob Player A wins a point>>>'))
    probWinB = float(input('Please enter the prob Player B wins a point>>>'))
    nGames = int(input('How many games should we play?>>>'))
    return probWinA, probWinB, nGames

def simulateNGames(probWinA, probWinB, nGames):
    gamesAWon = 0
    gamesBWon = 0

    for g in range(nGames):
        scoreA, scoreB = simulateOneGame(probWinA, probWinB)

        if scoreA > scoreB:
            gamesAWon += 1
        else:
            gamesBWon += 1

    return gamesAWon, gamesBWon

def simulateOneGame(probWinA, probWinB):
    scoreA = 0
    scoreB = 0

    server = 'A'

    # Actually play a game in here: While game isn't over, play the game
    while not gameOver(scoreA, scoreB):
        # play one point
        if server == 'A':
            # if random.random() < 0.4
            if random.random() < probWinA:
                scoreA += 1
            else:
                server = 'B'
        else:
            if random.random() < probWinB:
                scoreB += 1
            else:
                server = 'A'

    return scoreA, scoreB

def gameOver(scoreA, scoreB):
    return scoreA >= 15 or scoreB >= 15 # Return True of False

def printResults(gamesAWon, gamesBWon):
    totalGames = gamesAWon + gamesBWon
    print('Player A won', gamesAWon, 'games (', 100*gamesAWon/totalGames, 'percent)')
    print('Player B won', gamesBWon, 'games (', 100*gamesBWon/totalGames, 'percent)')

def main():

    # 1. We print an introduction to users, instructing them what program does.
    # DONE!
    printInstructions()

    # 2. We ask the user to enter the probability that player A wins at a serve, another one
    # that Player B wins at a serve, and then number of gmaes in the championship.
    # DONE!
    probWinA, probWinB, nGames = getUserInput()

    # 3. Simulate the games
    # NOT DONE!
    gamesAWon, gamesBWon = simulateNGames(probWinA, probWinB, nGames)

    # 4. Print out the results: how many games player A and player B won the championship
    # DONE!
    printResults(gamesAWon, gamesBWon)

if __name__ == '__main__':
    main()
