# TODO: copy the below to the test file you are working on.
# TODO: name the file depending on the function name.
# TODO:  the file name should start with 'test_'

import unittest
from gradescope_utils.autograder_utils.decorators import visibility, partial_credit
from BaseClass import BaseClass

# TODO:  modify the below variables depending on the test cases covering all the edge cases
# refer the assert statements for this function in the 'final' directory of the repo, to curate these tests

priority_scale0 = {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}

priority_scale1 = {
    'L1': "Lowest",
    'L2': "Low",
    'M': "Medium",
    'H1': "High",
    'H2': "Highest"
}

the_menu = {
    "E" : "Encrypt a message",
    "D" : "Decrypt a message",
    "S" : "Save encryption to file",
    "R" : "Retrieve decryption from file",
    "Q" : "Quit this program"} # TODO 1: add the options from the instructions

cipher_menu = {
    "T": "Scytale Cipher",
    "V": "Vigenere Cipher"
}


# note that
#  - if the function is accepting only parameter, the test case would look something like ->  (param1, )
#  - if the function is accepting two or more parameters, it would be like -> (param1, param2)
# - if the function does not require any parameter, it would go like -> ()
# TODO: below is the list of all the tests as a list. The params for each test case that need to be passed to the function.
# TODO : we need to add 5 test cases
param_list = [#(priority_scale0, ),
              #(priority_scale1, ),
              (the_menu, ),
              (cipher_menu, )
              ]

max_score = len(param_list)

# TODO:  name the class according to the function name being tested
class PrintMenu_TestComplex(BaseClass):

    """
    this is listed in config.py
    function_num = 0 => first function of the project
    """
    # tests print_menu()

    @partial_credit(max_score)
    @visibility('visible')
    def test1(self, set_score=None):
        # TODO: update the docstring based on the function name. This is what the students see when the test is runnning.
        """ print_menu()"""
        # TODO:  refer 'current_correct_fun_names' in the config.py file to get the 'function_num' for this function
        # TODO:  if the function you are testing has not been defined in the config.py file, just give it some number
        # TODO:  and let the CAD know so that s/he can add it there later.
        function_num = 0

        # TODO: everything below remains unchanged and can be used as is.
        input_line = f"2\n2\n"
        student_module = self.student_tasks
        total_score = max_score
        for params in param_list:
            if not self.handle_test_print_return_value(params, function_num, input_line, student_module):
                total_score -= 0.5
#             if not self.handle_test_function_logic(params, function_num, input_line, student_module):
#                 total_score -= 0.5

        set_score(total_score)
        if total_score == max_score:
            print("Congratulations! You passed this test.")


if __name__ == '__main__':
    unittest.main()
