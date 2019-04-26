from openpyxl import load_workbook

invalid_mentee = []

# restrictions need to be tweaked
MAX_MENTEE_ID = 748000
MIN_MENTEE_ID = 747000

MAX_MENTOR_ID = 150
MIN_MENTOR_ID = 0


def matching():
	mentor_book = load_workbook("2018-2019 REX_ Applicant Ranking.xlsx")
	mentee_book = load_workbook("2018 - 2019 REX Mentee Application.xlsx")

	mentee = mentee_book.active
	mentor = mentor_book.active

	mentee_info = parse_mentee(mentee)

	print(mentee_info)
	print(invalid_mentee)

def parse_mentee(mentee):

	mentee_number = []
	mentee_first_choice = []
	mentee_second_choice = []
	mentee_third_choice = []
	mentee_fourth_choice = []
	mentee_fifth_choice = []
	mentee_info = []
	i = 2

	while mentee.cell(row=i, column=6).value != None: 
		mentee_number.append(mentee.cell(row=i, column=6).value) # column 6 is F (URO Number)
		mentee_number[i-2], flag = checkValid(mentee_number[i-2], MAX_MENTEE_ID, MIN_MENTEE_ID)
		if flag: 
			invalid_mentee.append(mentee_number[i-2])
			i += 1
			continue

		mentee_first_choice.append(mentee.cell(row=i, column=15).value) # column 15 is O (First Choice)
		mentee_first_choice[i-2], flag = checkValid(mentee_first_choice[i-2], MAX_MENTOR_ID, MIN_MENTOR_ID)
		if flag: 
			invalid_mentee.append(mentee_number[i-2])
			i += 1
			continue

		mentee_second_choice.append(mentee.cell(row=i, column=18).value) # column 18 is R (Second Choice)
		mentee_second_choice[i-2], flag = checkValid(mentee_second_choice[i-2], MAX_MENTOR_ID, MIN_MENTOR_ID)
		if flag: 
			invalid_mentee.append(mentee_number[i-2])
			i += 1
			continue

		mentee_third_choice.append(mentee.cell(row=i, column=21).value) # column 21 is U (Third Choice)
		mentee_third_choice[i-2], flag = checkValid(mentee_third_choice[i-2], MAX_MENTOR_ID, MIN_MENTOR_ID)
		if flag: 
			invalid_mentee.append(mentee_number[i-2])
			i += 1
			continue

		mentee_fourth_choice.append(mentee.cell(row=i, column=24).value) # column 24 is X (Fourth Choice)
		mentee_fourth_choice[i-2], flag = checkValid(mentee_fourth_choice[i-2], MAX_MENTOR_ID, MIN_MENTOR_ID)
		if flag: 
			invalid_mentee.append(mentee_number[i-2])
			i += 1
			continue

		mentee_fifth_choice.append(mentee.cell(row=i, column=27).value) # column 27 is AA (Fifth Choice)
		mentee_fifth_choice[i-2], flag = checkValid(mentee_fifth_choice[i-2], MAX_MENTOR_ID, MIN_MENTOR_ID)
		if flag: 
			invalid_mentee.append(mentee_number[i-2])
			i += 1
			continue

		# mentee_info[i-1].appned(mentee_number[i-1], mentee_first_choice[i-1], mentee_second_choice[i-1], mentee_third_choice[i-1], mentee_fourth_choice[i-1], mentee_fifth_choice[i-1])
		mentee_info.append(mentee_number[i-2])

		i += 1

	return mentee_info

def checkValid(value, max, min):
	if type(value) == float and value >= min and value <= max: 
		return int(value), False
	else:
		if type(value) == float:
			return int(value), True
		return value, True

matching()