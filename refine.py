import csv

tee = open('Mentee.csv', mode='r', encoding='utf-8-sig')

readertee = csv.reader(tee)

menteeDict = {}
menteeArray = []

for row in readertee:
    val = []
    for i in range(1,6):
        if row[i]:
            val.append(row[i])

    menteeDict.update({row[0]:val})
    menteeArray.append(row)

tor = open('Mentor.csv', mode='r', encoding='utf-8-sig')

readertor = csv.reader(tor)

mentorDict = {}

for row in readertor:
    val = []
    for i in range(2,22):
        if row[i]:
            val.append(row[i])

    mentorDict.update({row[0]:val})

cap = open('Mentor.csv', mode='r', encoding='utf-8-sig')

readercap = csv.reader(cap)

capDict = {}

for row in readercap:
    capDict.update({row[0]:int(row[1])})

