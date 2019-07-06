import xlsxwriter

from matching import MentorMentee

import csv

tee = open('Mentee.csv', mode='r', encoding='utf-8-sig')

readertee = csv.reader(tee)

menteeDict = {}

for row in readertee:
    val = []
    for i in range(1,6):
        if row[i]:
            val.append(row[i])

    menteeDict.update({row[0]:val})

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


# mentee_prefs = {
#     "747033": ["88","87","60"],
#     "747021": ["88", "87", "60"],
#     "747457": ["88", "60", "87"],
# }

# mentor_prefs = {
#    "88": ["747033", "747021", "747457"],
#    "87": ["747033", "747021", "747457"],
#    "60": ["747033", "747457", "747021"]
# }

# capacities = {
#     "88": 2,
#     "87": 3,
#     "60": 1
# }

# game = MentorMentee.create_from_dictionaries(mentee_prefs, mentor_prefs, capacities)

# missing numbers: 4,17,54,57

game = MentorMentee.create_from_dictionaries(menteeDict, mentorDict, capDict)

print(game.solve())