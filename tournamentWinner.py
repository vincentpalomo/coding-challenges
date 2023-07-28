HOME_TEAM_WON = 1


def tournamentWinner(competitions, results):
    # create variable to keep track of current best team
    currentBestTeam = 'n/a'

    # create an object to store each teams scores, starting with an empty team and 0 score
    scores = {currentBestTeam: 0}

    for i, competition in enumerate(competitions):
        # get result of the current competition round
        result = results[i]
        # extract the names of the home and away teams
        home, away = competition

        # determine the winning team based on the result
        winningTeam = home if result == HOME_TEAM_WON else away

        # update the winning team's score by adding 3 points
        updateScores(winningTeam, 3, scores)

        # check if the winning team's score is greater than the current best team's score
        if scores[winningTeam] > scores[currentBestTeam]:
            # update the current best team to the winning team
            currentBestTeam = winningTeam

    return currentBestTeam


def updateScores(team, points, scores):
    # if team is not present in the scores object, add it with an initial value of 0
    if team not in scores:
        scores[team] = 0

    # update the teams score by adding the given amount of points
    scores[team] += points


competitions = [
    ['python', 'java'],
    ['java', 'javascript'],
    ['python', 'c#']
]

results = [0, 0, 1]
results2 = [1, 0, 1]

ret = tournamentWinner(competitions, results)
ret2 = tournamentWinner(competitions, results2)

print('winner round 1 is: ', ret)
print('winner round 2 is: ', ret2)
