import os
import datetime

print("Starting... hello people ")
print(str(datetime.datetime.today()))

def getCommitsCount(weekday):
    currentDay = weekday
    normalizedDay = currentDay + 1
    if currentDay == 6:
        normalizedDay = 0
    return abs(normalizedDay - 3) + 1

commitsCount = getCommitsCount(datetime.datetime.today().weekday())

print("commitsCount " + str(commitsCount))


def doGitStuff():
    for i in range(commitsCount):
        print("do commit")

        os.system("git pull")

        with open("state", 'a') as file:
            file.write("\ni:" + str(i) + " " + str(datetime.datetime.today()))

        os.system("git add . && git commit -m \"update calendar\" && git push -u origin")

doGitStuff()

print("finished, I hope that everything is ok")
