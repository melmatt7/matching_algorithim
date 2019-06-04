from matching import MentorMentee

# import csv

# tee = open('Mentee.csv', mode='r')

# readertee = csv.reader(tee)

# menteeDict = {}

# for row in readertee:
#     val = []
#     for i in range(1,5):
#         if row[i]:
#             val.append(row[i])

#     menteeDict.update({row[0]:val})

# print(menteeDict)

# tor = open('Mentor.csv', mode='r')

# readertor = csv.reader(tor)

# mentorDict = {}

# for row in readertor:
#     val = []
#     for i in range(2,20):
#         if row[i]:
#             val.append(row[i])

#     mentorDict.update({row[0]:val})

# print(mentorDict)

# cap = open('Mentor.csv', mode='r')

# readercap = csv.reader(cap)

# capDict = {}

# for row in readercap:
#     capDict.update({row[0]:row[1]})

# print(capDict)


mentee_prefs = {
    "747033": ["88","87","60"],
    "747021": ["88", "87", "60"],
    "747457": ["88", "60", "87"],
}

mentor_prefs = {
   "88": ["747033", "747021", "747457"],
   "87": ["747033", "747021", "747457"],
   "60": ["747033", "747457", "747021"]
}

capacities = {
    "88": 2,
    "87": 3,
    "60": 1
}

game = MentorMentee.create_from_dictionaries(mentee_prefs, mentor_prefs, capacities)

print(game.solve())