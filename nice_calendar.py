import os
import datetime


fileName = "state"

currentDay = datetime.datetime.today().weekday()

commitsCount = currentDay + 2
if currentDay == 6:
    commitsCount = 1

print("commitsCount " + str(commitsCount))

for i in range(commitsCount):
    print("do commit")

    os.system("git pull")

    with open(fileName, 'a') as file:
        file.write("commit")

    os.system("git add . && git commit -m \"update calendar\" && git push -u origin")

print("finished, I hope that everything is ok")