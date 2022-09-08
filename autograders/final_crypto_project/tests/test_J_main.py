import random


import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility, number, partial_credit
import config
from BaseClass import BaseClass

### New line and `Q` are added below to generate input_val
param_list = [
        # invalid cases
        ["L"],
        ["L", "K"],
        # encrypt cases
##        ["E", "T", "hello world", "4"],
##        ["E", "V", "helloworld", "hello"],
##        # decrypt
##        ["D", "T", "hello world", "4"],
##        ["D", "V", "helloworld", "hello"],
##        # restore
##        ["R", "test.csv", "y",
##         "missing-date.csv", "y",
##         "combined.csv", "y",
##         "single-task.csv","n"],
##        # save
##        ["S", "invalid", "y",
##         "my-tasks.csv"],
    ]
each_case_weight = 0.5
max_score  = len(param_list)*each_case_weight


class J_main(BaseClass):

    """
    this is to test the main.py file for console input/output
    """

    @partial_credit(max_score)
    @visibility('visible')
    def test1(self, set_score=None):
        """main module input/output. """

        total_score = max_score
        for params in param_list:
            input_val = "\n".join(params) + "\n\nQ\n"
            # if not self.handle_module_io(input_val):
            #     total_score -= each_case_weight
            if not self.handle_infinite(self.handle_module_io, (input_val, )):
                total_score -= each_case_weight
        set_score(total_score)
        if total_score == max_score:
            print("Congratulations! You passed this test.")


if __name__ == '__main__':
    unittest.main()

