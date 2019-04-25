import numpy

def matching():
	mentee=open('mentee.txt','r')
	mentor=open('mentor.txt','r')
	result=open('result.txt', 'w')
	result1=open('result1.txt', 'w')

	mentor_info = parse_val(mentor)
	mentee_info = parse_val(mentee)

	for m in range(0,len(mentee_info)):
		for n in range(0,len(mentee_info[m])):
			result.write('%s ' % mentee_info[m][n])
		result.write('\n')

	for f in range(0,len(mentor_info)):
		for g in range(0,len(mentor_info[f])):
			selection = get_match(mentor_info[f])
			result1.write('%s ' % mentor_info[f][g])
		result1.write('\n')

def parse_val(file): 
	id = ''
	choices = ''
	info = []

	for line in file:

		file_val=[]
		i=0
		while line[i] != '\t':
			id += line[i]
			i += 1
		file_val.append(id)
		id = ''

		while line[i] != '\n':
			if line[i] == '\t':
				i += 1
			else:
				while line[i] != '\t' and line[i] != '\n':
					choices += line[i]
					i += 1
				file_val.append(choices)
				choices = ''		

		info.append(file_val)

	return info


def get_match(mentor_pref):
	mentor_id = mentor_pref[0]
	
	mentor_size = mentor_pref[1]


matching()