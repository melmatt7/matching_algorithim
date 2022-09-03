from context import matching_algo

import unittest
import io

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_simple_matching(self):
        mentee_file = '../matching_algo/files/test_files/mentee_test.csv'
        mentor_file = '../matching_algo/files/test_files/mentor_test.csv'

        menteeDict, mentorDict, capDict = matching_algo.extract_dict(mentee_file, mentor_file)

        game = matching_algo.MentorMentee.create_from_dictionaries(menteeDict, mentorDict, capDict)
        res_data = game.solve()

        matching_algo.write_results(res_data, "test_files/result_test_basic")

        self.assertListEqual(
            list(io.open('../matching_algo/files/test_files/result_test_basic.csv')),
            list(io.open('../matching_algo/files/test_files/result_test_basic_ref.csv')))


if __name__ == '__main__':
   unittest.main()