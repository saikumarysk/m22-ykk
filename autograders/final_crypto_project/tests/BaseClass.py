import sys
import difflib as dl
import importlib
from io import StringIO
import time

from copy import deepcopy
import unittest

import config
import correct
import runpy

from multiprocessing import Process

class Mylist(int):
    pass

process_result = "result"

def annotated(num, name, docstring):
    r = Mylist(num)
    setattr(r, "__name__", name)
    setattr(r, "__doc__", docstring)
    return r


def get_last_next(exception_traceback):
    """
    This function will go through the stack trace and
    get the line of error for us.
    Just recursion, no need to change
    """
    if exception_traceback.tb_next is not None:
        return get_last_next(exception_traceback.tb_next)
    return exception_traceback.tb_lineno

star_line = "\n******************************************************\n"

class BaseClass(unittest.TestCase):
    
    ################## SETUPS (imports and selecting modules)  ######################
    @classmethod
    def setUpClass(cls):
        """
        This method is for work ones before all tests
        """
        # cls.filename_tasks = config.required_files[1][:-3]  # remember to remove the .py extension
        # cls.filename_validate = config.required_files[2][:-3]  # remember to remove the .py extension
        #
        # cls.student_tasks = cls.import_module_util(cls.filename_tasks)
        # cls.student_validate = cls.import_module_util(cls.filename_validate)
        cls.filename_tasks = config.required_files[1][:-3]  # remember to remove the .py extension
        cls.student_tasks = cls.import_module_util(cls.filename_tasks)

    @classmethod
    def import_module_util(cls, filename):
        try:
            temp_module = importlib.import_module(filename)
        except ModuleNotFoundError as e:
            if filename in e.msg:
                temp_module = "Unable to find your file. Is it named correctly?"
            else:
                temp_module = f"We found some unexpected import, python says:\n{e.msg}\n"
        except (TypeError, ValueError) as e:
            temp_module = f"Syntax error: \n{e}"
        except AssertionError as e:
            temp_module = f"Assertion error: \n{e}"
        except Exception as e:
            temp_module = f"Unexpected exception error: \n{e}"
        return temp_module

    def setUp(self) -> None:
        if type(self.student_tasks) == str:
            self.fail(f"There is an error in {self.filename_tasks}.py:\n{self.student_tasks}\n")

    ################## DO NOT CHANGE ME, I AM HELPER, CHANGE ABOVE ME ########################
    def handle_test_function_logic(self, params, function_name, input_line, student_module):
        '''
        this function is used to test the value returned by the function in the student's code and compare it with
        that returned by our implementation in the correct.py file
        '''
        ############### CORRECT PART #####################
        corr_params, corr_stdout, expected_answer, stud_stdout, student_answer = self.handle_test_util(function_name,
                                                                                                       input_line,
                                                                                                       params,
                                                                                                       student_module)

        ############### END STUDENT PART #####################

        ############### CHECK PART #####################
        # if student_answer is None:
        #     self.fail(f"Do you have a return statement in the right place?")
        parameters_to_show = "(" + ', '.join(str(i) for i in params) + ")"
        output = []
        output.append(star_line)
        output.append(f"Input arguments:\n\n{parameters_to_show}\n")
        output.append("Check for function logic.")
        is_correct = True

        if expected_answer != student_answer:
            output.append(f"Your function returned:\n"
                  f"{student_answer} {type(student_answer)}\n"
                  f"but expected:\n"
                  f"{expected_answer} {type(expected_answer)}\n"
                  f"\nIf you don't see the difference, the issue might be in the types of the returned objects.\n")
            is_correct = False

        if params != corr_params:
            output.append(f"It looks like you modified the input parameters incorrectly.\n"
                      f"We expected to see \n'{corr_params}'\n"
                      f"but we saw \n'{params}'\n")
            is_correct = False

        # student_print = stud_stdout.getvalue()
        # expected_print = corr_stdout.getvalue()
        # 
        # if expected_print != "":
        #     if student_print != expected_print:
        #         output.append(f"The expected output is\n>>>\n{expected_print}\n<<<\n"
        #                   f"yours is \n>>>\n{student_print}\n<<<\n"
        #                   f"\nIf you don't see the difference, the issue might be in the spacing.\n"
        #                   f"Use an online text comparison tool to check the difference.\n")
        #         is_correct = False

        output.append(star_line)
        if not is_correct:
            print('\n'.join(output))
        return is_correct

    def handle_test_print_return_value(self, params, function_num, input_line, student_module):
        '''
        this function is used to handle the console output from the print statements from the function in the student's code
        and compare it with that of our implementation in the correct.py file
        '''
        ############### CORRECT PART #####################
        corr_params, corr_stdout, expected_answer, stud_stdout, student_answer = self.handle_test_util(function_num,
                                                                                                       input_line,
                                                                                                       params,
                                                                                                 student_module)
        parameters_to_show = "(" + ', '.join(str(i) for i in params) + ")"
        output = []
        output.append(star_line)
        output.append(f"Input arguments: \n\n{parameters_to_show}\n")
        output.append("Check for print statements and return type.")
        if student_answer is None and expected_answer is not None:
            output.append(f"Do you have a return statement in the right place?")

        student_print = stud_stdout.getvalue()
        expected_print = corr_stdout.getvalue()
        is_correct = True
        if expected_print != "":
            if student_print != expected_print:
                # output.append(f"The expected output is\n>>>\n{expected_print}\n<<<\n"
                #       f"yours is \n>>>\n{student_print}\n<<<\n"
                #       f"\nIf you don't see the difference, the issue might be in the spacing.\n"
                #       f"Use an online text comparison tool to check the difference.\n")
                output.append("Your output does not match the expected output.\n")
                output.append("Find the diff below.\n\n"
                      "'+' implies missing string that needs to be added.\n"
                      "'-' implies unexpected string that needs to be removed.\n\n")
                ct = 0
                for diff in dl.unified_diff(student_print.split('\n'), expected_print.split('\n')):
                    ct += 1
                    if ct < 4:
                        continue
                    output.append(diff)
                is_correct = False

        elif student_print != "":
            output.append(f"You should not have any print() inside the function!\n")
            is_correct = False

        output.append(star_line)
        if not is_correct:
            print('\n'.join(output))
        return is_correct

    def handle_test_util(self, function_num, input_line, params, student_module):
        '''
        this is just a util function that is used by the
        handle_test_print_return_value and handle_test_function_logic function to execute the student's code for the
        given function.
        '''
        corr_params, corr_stdout, expected_answer = self.get_expected_result(function_num, input_line, params)

        stud_stdout, student_answer = self.get_student_result(function_num, input_line, params, student_module)
        ############### CHECK PART #####################
        # if student_answer is None:
        #     self.fail(f"Do you have a return statement in the right place?")
        return corr_params, corr_stdout, expected_answer, stud_stdout, student_answer

    def get_student_result(self, function_num, input_line, params, student_module):
        parameters_to_show = "(" + ', '.join(str(i) for i in params) + ")"
        ###############END OF CORRECT PART #####################
        ############### STUDENT PART #####################
        student_func_name = config.current_fun_names[function_num]
        if type(student_module) == str:
            self.fail(f"There is an error in your code:\n" \
                      f"{student_module}\n")
        try:
            student_fun = getattr(student_module, student_func_name)
        except Exception as e:
            self.fail(
                f"We caught the following error caused by your code, \n"
                f"when importing {student_func_name}:\n{e} \n"
                f"The input that we provided was:"
                f"\n{parameters_to_show}\n"
                f"{star_line}"
            )
        # Define the string (strings inside one variable)
        # that will be what the student code reads via input()
        to_input = input_line
        # Save the previous area where print() will go, and create our own
        old_stdout = sys.stdout
        sys.stdout = stud_stdout = StringIO()
        # Assign the new area where from student will get their input()
        example_input = to_input  # This is the line that we created
        old_stdin = sys.stdin
        s = StringIO(example_input)
        sys.stdin = s
        try:
            student_answer = student_fun(*params)
        except Exception as e:
            self.fail(
                f"We caught the following error caused by your code:\n{e}"
                f"\n\nCheck the following:\n"
                f" - Incorrect number or type of parameters/arguments?\n"
                f" - Error inside the function? Did you run your code?\n"
                f" - Used some global scope variables?\n\n"
                f"The input that we provided was:\n"
                f"`{parameters_to_show}`\n"
                f"{star_line}"
            )
        except KeyError as e:
            self.fail(
                f"We caught the following **KeyError** caused by your code:\n{e}"
                f"\n\nCheck the following:\n"
                f" - Where are you using a dictionary?\n"
                f" - Did you run your code with sample inputs?\n"
                f" - Are your input arguments of the correct type?\n\n"
                f"The input that we provided was:\n"
                f"`{parameters_to_show}`\n"
                f"{star_line}"
            )
        except IndexError as e:
            self.fail(
                f"We caught the following **IndexError** caused by your code:\n{e}"
                f"\n\nCheck the following:\n"
                f" - Where are you using a list?\n"
                f" - Did you run your code with sample inputs?\n"
                f" - Are your input arguments of the correct type?\n\n"
                f"The input that we provided was:\n"
                f"`{parameters_to_show}`\n"
                f"{star_line}"
            )
        finally:
            # restore the print() area anyway, or all tests will fails
            sys.stdout = old_stdout
            sys.stdin = old_stdin
        ############### END STUDENT PART #####################
        return stud_stdout, student_answer

    def get_expected_result(self, function_num, input_line, params):
        correct_func = getattr(correct, config.current_correct_fun_names[function_num])
        to_input = input_line
        # Save the previous area where print() will go, and create our own
        old_stdout = sys.stdout
        sys.stdout = corr_stdout = StringIO()
        # Assign the new area where from student will get their input()
        example_input = to_input  # This is the line that we created
        old_stdin = sys.stdin
        s = StringIO(example_input)
        sys.stdin = s
        corr_params = deepcopy(params)
        ##!
        expected_answer = correct_func(*corr_params)
        ##!
        sys.stdout = old_stdout
        sys.stdin = old_stdin
        return corr_params, corr_stdout, expected_answer

    # DO NOT TOUCH THIS
    def runner(self, fun, pars, input_line=""):

        to_input = input_line
        # Save the previous area where print() will go, and create our own
        old_stdout = sys.stdout
        sys.stdout = module_stdout = StringIO()
        # Assign the new area where from student will get their input()
        example_input = to_input  # This is the line that we created
        old_stdin = sys.stdin
        s = StringIO(example_input)
        sys.stdin = s
        try:
            result = fun(*pars)
        except Exception as e:
            raise e
        finally:
            sys.stdout = old_stdout
            sys.stdin = old_stdin

        return result, module_stdout.getvalue()

    def handle_module_io(self, input_val):
        # the_menu = {'L': 'List', 'A': 'Add', 'U': 'Update', 'D': 'Delete',
        #             'S': 'Save the data', 'R': 'Restore data from file', 'Q': 'Quit this program'}

        # TODO: Create list of changing parameters, preferably all possible in theory
        # cases_to_test = list(menu.keys()) + ["Broken one"]
        # Keep it list with one value if that is the only one to test
        # cases_to_test = ["Q"]

        correct_main = getattr(correct, "main")

        # for input_vals in cases_to_test:
            # Each run will be with different option from all possible parameters
            # Keep it tuple, if it is one parameter in target function
            # parameters = (option,)
        expected_result, expected_output = self.runner(correct_main, [], input_val)
        res = True
        try:
#student_result, student_output = self.runner(runpy.run_module, ["task_system", None, "__main__"], input_val)
            student_result, student_output = self.runner(runpy.run_module, [config.main_program_module, None, "__main__"], input_val)
        except Exception as e:
            print(star_line)
            print(f"Input arguments: \n\n{input_val}\n")
            print(f"We ran into an error while running your code.\nPython says:\n{e}")
            if 'EOF when reading a line' in str(e):
                # the below output is specific to the menu driven questions and not generic.
                print("Seems like you the placement of input() statements in your code is incorrect.\n"
                      "Or maybe there is an infinite loop that does not break when the user tries to quit.\n"
                      "Please read the instructions carefully.")
            print(star_line)
            res = False
        else:
            if student_output != expected_output:
                print(star_line)
                print(f"Input arguments:\n\n{input_val}\n")
                student_output = student_output if student_output else "<Empty>"
                expected_output = expected_output if expected_output else "<Empty>"
                # print(f"The expected output is\n>>>\n{expected_output}\n<<<\n"
                #       f"yours is \n>>>\n{student_output}\n<<<\n"
                #       f"\nIf you don't see the difference, the issue might be in the spacing.\n"
                #       f"Use an online text comparison tool to check the difference.\n")
                print("Your output does not match the expected output. \n")
                print("Find the diff below.\n\n"
                      "'+' implies missing string that needs to be added.\n"
                      "'-'  implies unexpected string that needs to be removed.\n\n")
                ct = 0
                for diff in dl.unified_diff(student_output.split('\n'), expected_output.split('\n')):
                    ct += 1
                    if ct < 4:
                        continue
                    print(diff)
                print(star_line)
                res = False
        # print(f"Well done, you got it!")
        return res

    @staticmethod
    def handle_infinite(func, args):
        '''
        use this function if the student solution is suspected to have an infinite loop
        usage : handle_infinite(handle_test_print_return_value, args)
        where 'args' is basically the list of arguments that we need to pass to 'func'
            '''
        args = tuple(args)
        p = Process(target=func, args=args)
        p.start()
        # duration within which we want the test to be over.
        max_time = 5
        total_time = 0
        while p.is_alive() and total_time < max_time:
            total_time += 0.2
            time.sleep(0.2)

        if p.is_alive():
            print(star_line)
            print(f"Infinite loop detected. Process is still running after {max_time} seconds."
                  )
            print(star_line)
            p.terminate()
            return False
        else:
            ''' if no infinite loop was detected, rerun the test, this time in the main process.'''
            return func(*args)

#####################################################################################################################

if __name__ == '__main__':
    unittest.main()
