import os
import datetime

currentDay = 0

fileName = "state"

if not os.path.exists(fileName):
    with open(fileName, 'w'): pass

print(currentDay)

currentDay = datetime.datetime.today().weekday()

commitsCount = currentDay + 2
if currentDay == 6:
    commitsCount = 1

