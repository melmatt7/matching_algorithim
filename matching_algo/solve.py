from matching import MentorMentee
from csv_utils import extract_dict
from csv_utils import write_results
import numpy as np

mentee_file = 'files/selections/mentee_2023.csv'
mentor_file = 'files/selections/mentor_2023.csv'

menteeDict, mentorDict, capDict = extract_dict(mentee_file, mentor_file)

# menteeDict = {
#     "747033": ["88","87","60"],
#     "747021": ["88", "87", "60"],
#     "747457": ["88", "60", "87"],
# }

# mentorDict = {
#    "88": ["747033", "747021", "747457"],
#    "87": ["747033", "747021", "747457"],
#    "60": ["747033", "747457", "747021"]
# }

# capDict = {
#     "88": 2,
#     "87": 3,
#     "60": 1
# }

# game = MentorMentee.create_from_dictionaries(mentee_prefs, mentor_prefs, capacities)

game = MentorMentee.create_from_dictionaries(menteeDict, mentorDict, capDict)
print(sum(capDict.values()))
print(206/244)

res_data = game.solve()

write_results(res_data, "result_2023")