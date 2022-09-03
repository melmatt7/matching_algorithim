import csv

def extract_dict(mentee_file, mentor_file):

    tee = open(mentee_file, mode='r', encoding='utf-8-sig')

    readertee = csv.reader(tee)

    menteeDict = {}
    menteeArray = []

    for row in readertee:
        val = []
        for i in range(1,len(row)):
            if row[i]:
                val.append(row[i])

        menteeDict.update({row[0]:val})
        menteeArray.append(row)

    tor = open(mentor_file, mode='r', encoding='utf-8-sig')

    readertor = csv.reader(tor)

    capDict = {}
    mentorDict = {}

    for row in readertor:
        val = []
        capDict.update({row[0]:int(row[1])})
        for i in range(2,len(row)):
            if row[i]:
                val.append(row[i])

        mentorDict.update({row[0]:val})

    return menteeDict, mentorDict, capDict
