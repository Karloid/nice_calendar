import os
import datetime

fileName = "state"

today = datetime.datetime.today()
currentDay = today.weekday()

commitsCount = currentDay + 2
if currentDay == 6:
    commitsCount = 1

print("commitsCount " + str(commitsCount))

for i in range(commitsCount):
    print("do commit")

    os.system("git pull")

    with open(fileName, 'a') as file:
        file.write("\ni:" + str(i) + str(today))

    os.system("git add . && git commit -m \"update calendar\" && git push -u origin")

print("finished, I hope that everything is ok")
