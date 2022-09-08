"""
Tests that all files from config.versions submitted
"""
import unittest
from gradescope_utils.autograder_utils.decorators import weight, partial_credit

# https://github.com/gradescope/autograder_samples/blob/master/python/src/tests/test_files.py
from gradescope_utils.autograder_utils.files import check_submitted_files

import config


class A_Files_Exist(unittest.TestCase):
    @weight(1)
    def test_submitted_files(self, set_score=None):
        """Check required files"""
        # The above docstring will be shown on Gradescope

        if config.autograder_logging == 1:
            print('USE THIS IF YOU WANT TO WRITE TO HIDDEN OUTPUT', file=config.hidden_stdout)

        # Set required files
        required_files = config.required_files

        for rf in required_files:
            if rf not in config.student_submitted_files:
                self.fail(f'You have not submitted all required files.\n\n' + 
                f'Required files are:\n{required_files}\n\n' + 
                f'You have submitted the following files:\n{config.student_submitted_files}\n\n' + 
                f'You are missing at least "{rf}".\n' + 
                f'Make sure that you submit *all* files at the *same* time.')

        # Below print will be shown when correct
        print('All required files are submitted!')


if __name__ == '__main__':
    unittest.main()
