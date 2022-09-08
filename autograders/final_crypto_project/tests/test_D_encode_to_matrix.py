# TODO: copy the below to the test file you are working on.
# TODO: name the file depending on the function name.
# TODO:  the file name should start with 'test_'

import unittest
from gradescope_utils.autograder_utils.decorators import visibility, partial_credit
from BaseClass import BaseClass
import random

# note that
#  - if the function is accepting only parameter, the test case would look something like ->  (param1, )
#  - if the function is accepting two or more parameters, it would be like -> (param1, param2)
# - if the function does not require any parameter, it would go like -> ()

### Provided asserts
param_list = [("CSWEIGHT TEACHES US PROGRAMMING", 5),
              ("YELLOW SUBMARINE", 2),
                ("CHECK OUT THE HOOK WHILE MY DJ REVOLVES IT", 9),
                ("I LIKE CRYPTOGRAPHY", 19),
              ]

max_score = len(param_list)


########################################################################
### Create parameters for a randomized set of tests
sample_info = ["In a world where you can be anything, be kind.",
                "He who asks a question is a fool for five minutes; he who does not ask a question remains a fool forever.",
                "Excellence is not a skill.",
                "Teachers can open the door, but you must walk through it yourself.",
                "The mind is not a vessel to be filled but a fire to be ignited.",
                "Procrastination makes easy things hard and hard things harder.",
                "The expert in anything was once a beginner.",
                "There are no shortcuts to any place worth going.",
                "Motivation is what gets you started. Habit is what keeps you going."
]

num_rand_tests = 5
rand_param_list = []
for test in range(num_rand_tests):
        rand_msg = random.choice(sample_info)
        rand_key = random.randint(2, len(rand_msg)-1)
        rand_param_list.append((rand_msg, rand_key))


##rand_letter = chr(random.randint(ord('a'), ord('z')))
##rand_name = rand_letter * random.randint(1, 35)
##
##rand_dates = []
##num_dates = 8
##for count in range(num_dates):
##    day = random.randint(0, 62) # indentionally outside the normal range
##    day = f"{day:0>2}"
##    month = random.randint(0, 19)
##    month = f"{month:0>2}"
##    year = random.randint(100, 2555)
##    date = f"{month}/{day}/{year}"
##    rand_dates.append(date)

rand_max_score = len(rand_param_list)
########################################################################


# TODO:  name the class according to the function name being tested
class encode_to_matrix_TestComplex(BaseClass):

    """
    this is listed in config.py
    function_num = 0 => first function of the project
    """
    # tests encode_to_matrix()

    @partial_credit(max_score)
    @visibility('visible')
    def test1(self, set_score=None):
        """D1. encode_to_matrix() """
        # Function added to config.py
        function_num = 2

        # TODO: everything below remains unchanged and can be used as is.
        input_line = f"2\n2\n"
        student_module = self.student_tasks
        total_score = max_score
        for params in param_list:
            if not self.handle_test_print_return_value(params, function_num, input_line, student_module):
                total_score -= 0.5
            if not self.handle_test_function_logic(params, function_num, input_line, student_module):
                total_score -= 0.5

        set_score(total_score)
        if total_score == max_score:
            print("Congratulations! You passed this test.")

##    @partial_credit(rand_max_score)
##    @visibility('visible')
##    def test2(self, set_score=None):
##        """ update_task() empty + randomized"""
##        # Function added to config.py
##        function_num = 5
##
##        # TODO: everything below remains unchanged and can be used as is.
##        input_line = f"2\n2\n"
##        student_module = self.student_tasks
##        total_score = rand_max_score
##        for params in rand_param_list:
##            if not self.handle_test_print_return_value(params, function_num, input_line, student_module):
##                total_score -= 0.5
##            if not self.handle_test_function_logic(params, function_num, input_line, student_module):
##                total_score -= 0.5
##
##        set_score(total_score)
##        if total_score == rand_max_score:
##            print("Congratulations! You passed this test.")


if __name__ == '__main__':
    unittest.main()
