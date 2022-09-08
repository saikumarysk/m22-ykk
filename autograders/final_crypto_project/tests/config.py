"""
This file can be used to define the "global" variables
that apply to the other separate test files.
Order of other files is defined by the name of the FILE alphabetically.
"""
import os
import sys

# TURN LOGGING ON OR OFF
# 0 - OFF
# 1 - ON
autograder_logging = 1

hidden_stdout = sys.stdout
# TODO 1. Create tests from asserts
# 2. Create file-stored check with many options
# 3. Check the output
# 4. Check the docstrings

# TODO:  use the numbers in the comments after each function name to
# reference it in the test_ files -- see the function_num variable there
current_fun_names = [
    'print_menu', # 0
    'create_matrix', # 1
    'encode_to_matrix', # 2
    'encrypt_transposition', # 3,
    'decrypt_transposition', # 4
    'extend_string', # 5
    'extend_vigenere', # 6
    'get_alphabet_vigenere', # 7
    'encrypt_vigenere', # 8
    'decrypt_vigenere', # 9
     ]

current_correct_fun_names = current_fun_names # needed by the BaseClass to run tests in test_ files

# TODO: Change for current assignment
# TODO: Adapt the scores as per the quiz
num_pts_file_name = 1
num_pts_fn_name = 1
num_pts_docstring = 1
num_pts_global_vars = 1
num_pts_simple_test = 2
num_pts_randomized_test = 2
num_pts_whole_program_run = 1
num_pts_version_check = 0

fun_names = []
for fun_name in current_fun_names:  # TODO: enable for the release
    fun_names.append([fun_name])

# TODO: add ALL required files
required_files = ['crypto_system.py', 'crypto_functions.py', 'crypto_tests.py'] 
main_program_module = required_files[0].replace(".py", "")
#print(main_program_module)
# File we will be running tests on
#main_functions_file = required_files[1] #

# List all the possible files that can be in the directory
# so that when we diff it with the contents of the submission
# the file that's left is the student's .py
test_files = ['__init__.py', 'requirements.txt', 'run_autograder',
              'setup.sh', 'tests', 'run_tests.py', 'results.json', "__pycache__",
              '__MACOSX', 'metadata.yml',  
             ".pytest_cache",  # this is for the purpose of local testing (not on gradescope)
              ".DS_Store",
              "BaseClass.py",
              "config.py",
              "__init__.py",
              "correct.py",
              "task_data1.csv",
              "task_data2.csv",
              "task_data3.csv",
              "submission examples",
              "test_A_files.py",
              "test_B_fun_names.py",
              "test_C_create_matrix.py",
              "test_D_encode_to_matrix.py",
              "test_E_print_menu.py",
              "test_F_delete.py",
              "test_G_load_from_csv_complex.py",
              "test_H_save_to_csv_complex.py",
              "test_I_get_written_date_complex.py",
              "test_is_valid_index.py",
              "test_J_main.py",
              "csv_saver.py"
              ]
# TODO: update the above depending on the names of the test files.
################################
all_submitted_files = set(os.listdir('.'))

# # Will be available globally to see which files were submitted by students
student_submitted_files = all_submitted_files - set(test_files)


if autograder_logging:
    print('STUDENT\'S SUBMITTED FILES:', student_submitted_files)
