import csv

tee = open('Mentee.csv', mode='r')

readertee = csv.reader(tee)

menteeDict = {}

for row in readertee:
    val = []
    for i in range(1,5):
        if row[i]:
            val.append(row[i])

    menteeDict.update({row[0]:val})

print(menteeDict)

tor = open('Mentor.csv', mode='r')

readertor = csv.reader(tor)

mentorDict = {}

for row in readertor:
    val = []
    for i in range(2,20):
        if row[i]:
            val.append(row[i])

    mentorDict.update({row[0]:val})

print(mentorDict)

cap = open('Mentor.csv', mode='r')

readercap = csv.reader(cap)

capDict = {}

for row in readercap:
    capDict.update({row[0]:row[1]})

print(capDict)