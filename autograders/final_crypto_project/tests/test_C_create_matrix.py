# TODO: copy the code below to the test file you are working on.
# TODO: name the file to include the function name.
# TODO:  the file name should start with 'test_'

import unittest
from gradescope_utils.autograder_utils.decorators import visibility, partial_credit
from BaseClass import BaseClass
import random

# TODO: modify the variables below, depending on the test cases covering all the edge cases
# refer to the assert statements for this function in the 'final' directory of the repo, to curate these tests

# note that
# - if the function is accepting only parameter, the test case would look something like ->  (param1, )
# - if the function is accepting two or more parameters, it would be like -> (param1, param2)
# - if the function does not require any parameter, it would go like -> ()
# TODO: below is the list of all the tests as a list.
# The list holds the params for each test case that need to be passed to the function.
# TODO : we need to add 5 test cases

### asserts from the instructions
param_list = [
    (2, 2),  # 2 rows, 2 columns
    (2, 3),   # 2 rows, 3 columns
    (7, 5), 
    (8, 2), 
    (0, 19),
    (5, 0), 
]

max_score = len(param_list)


########################################################################

# TODO:  name the class according to the function name being tested
class create_matrix_TestComplex(BaseClass):
    """
    this is listed in config.py
    function_num = 0 => first function of the project
    """
    # tests create_matrix()
    
    @partial_credit(max_score)
    @visibility('visible')
    def test1(self, set_score=None):
        # TODO: update the docstring based on the function name. This is what the students see on Gradescope as a test name.
        """create_matrix()"""
        # TODO:  refer 'current_correct_fun_names' in the config.py file to get the 'function_num' for this function
        # TODO:  if the function you are testing has not been defined in the config.py file, just give it some number
        # TODO:  and let the CAD know so that s/he can add it there later.
        function_num = 1

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

##    @partial_credit(num_tasks) # TODO: make sure this is correct
##    @visibility('visible')
##    def test2(self, set_score=None):
##        # TODO: update the docstring based on the function name. This is what the students see on Gradescope as a test name.
##        """ get_new_task() randomized"""
##        # TODO:  refer to the 'current_correct_fun_names' in the config.py file to get the 'function_num' for this function
##        # TODO:  if the function you are testing has not been defined in the config.py file, just give it some number
##        # TODO:  and let the CAD know so that s/he can add it there later.
##        function_num = 1
##
##        # TODO: everything below remains unchanged and can be used as is.
##        input_line = f"2\n2\n"
##        student_module = self.student_tasks
##        total_score = num_tasks # TODO: make sure this is correct
##        for params in rand_param_list: # TODO: make sure this is the correct list to loop over
##            if not self.handle_test_print_return_value(params, function_num, input_line, student_module):
##                total_score -= 0.5
##            if not self.handle_test_function_logic(params, function_num, input_line, student_module):
##                total_score -= 0.5
##
##        set_score(total_score)
##        if total_score == max_score:
##            print("Congratulations! You passed this test.")

if __name__ == '__main__':
    unittest.main()
