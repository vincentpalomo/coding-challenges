HOME_TEAM_WON = 1


def tournamentWinner(competitions, results):
    currentBestTeam = 'n/a'
    return currentBestTeam


competitions = [
    ['python', 'java'],
    ['java', 'javascript'],
    ['python', 'c#']
]

results = [0, 0, 1]

ret = tournamentWinner(competitions, results)

print('winner is: ', ret)
