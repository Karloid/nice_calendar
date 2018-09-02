import os
import datetime
from subprocess import call


fileName = "state"

currentDay = datetime.datetime.today().weekday()

commitsCount = currentDay + 2
if currentDay == 6:
    commitsCount = 1

commitsCount = commitsCount + 5 #just test


print("commitsCount " + str(commitsCount))

for i in range(commitsCount):
    print("do commit")

    os.system("git pull")

    with open(fileName, 'w') as file:
        file.write("commit")
        
    os.system("git add . && git commit -m \"update calendar\" && git push -u origin")

print("finished, hope everything is ok")