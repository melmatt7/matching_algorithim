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
                clean_row = row[i].strip()
                val.append(clean_row)

        menteeDict.update({row[0].strip():val})
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
                clean_row = row[i].strip()
                val.append(clean_row)

        mentorDict.update({row[0].strip():val})

    return menteeDict, mentorDict, capDict
