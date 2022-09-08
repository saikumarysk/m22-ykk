"""
Creates N testing functions for all config.fun_names
"""
import os
import unittest
from gradescope_utils.autograder_utils.decorators import weight, partial_credit
import importlib
import config
from ddt import ddt, data
from BaseClass import BaseClass

class Mylist(int):
    pass


def annotated(num, name, docstring):
    r = Mylist(num)
    setattr(r, "__name__", name)
    setattr(r, "__doc__", docstring)
    return r

number_of_functions = len(config.current_fun_names)
score_per_unit = 0.5

@ddt
class B_TestFunNames(BaseClass):

        # Here there will be created exactly as many tests as function names in config.fun_names
    # For 1pt weight for each existed function
    @partial_credit(number_of_functions * score_per_unit)
    def test(self, set_score=None):
        """Function definitions"""

        fun_names = config.current_fun_names
        dir_list = set(dir(self.student_tasks))
        fun_definition_absent = []
        fun_definition_present = []
        total_score = number_of_functions * score_per_unit
        for fun_name in fun_names:
            if fun_name not in dir_list:
                fun_definition_absent.append(fun_name)
                # self.fail(f"Did you correctly define {fun_name}?")
            else:
                # print(f"Function '{fun_name}' is defined")
                fun_definition_present.append(fun_name)
        if fun_definition_present:
            fun_present_str = '\n'.join(fun_definition_present)
            print(f"The following function definitions are present: \n{fun_present_str}\n\n")
        if fun_definition_absent:
            total_score -= len(fun_definition_absent)*score_per_unit
            fun_absent_str = '\n'.join(fun_definition_absent)
            print(f"The following function definitions are absent: \n{fun_absent_str}\n\n")
        set_score(total_score)

    @partial_credit(number_of_functions * score_per_unit)
    def test_doc_strings_in_funs(self, set_score=None):
        """Docstring presence"""
        fun_names = config.current_fun_names
        no_doc_string = []
        total_score = number_of_functions * score_per_unit
        for name in fun_names:
            try:
                function = getattr(self.student_tasks, name)
            except:
                no_doc_string.append(name)
                continue
            if not function.__doc__:
                no_doc_string.append(name)

        if no_doc_string:
            total_score -= len(no_doc_string) * score_per_unit
            s = "You do not have docstrings (or the whole function)\nfor the following functions:\n"
            for name in no_doc_string:
                s += "- " + name + "\n"
            s += "\nDid you create a proper doc string with \"\"\" or '''\n" \
                 "and place it directly underneath the function signature?\n"
            print(s)
        else:
            print("You do have a docstring for each function! Documentation is a great habit!")
        set_score(total_score)

    @weight(config.num_pts_global_vars)
    def test_e(self):
        """Variables outside the if-name-main"""
        
        allowed_imports = ["math", "string", "os", "random"]
        vars = [i for i in dir(self.student_tasks) if ("__" not in i) and (i not in allowed_imports)]
###        vars = [i for i in dir(self.student_tasks) if "__" not in i and i != "math"]

        for fun in config.current_fun_names:
            if fun not in vars:
                self.fail(f"Function '{fun}' is not found.")
            vars.pop(vars.index(fun))

        new_vars = []
        for var in vars:
            if not hasattr(getattr(self.student_tasks, var), "__call__"):
                new_vars.append(var)
        vars = new_vars
        if vars:
            s = "You have following "
            for var in vars:
                s += f"- {var}\n"
            s += "in global scope. It is a bad sign!"
            self.fail(s)

        print("No variables defined in global scope! Well done!")

if __name__ == '__main__':
    unittest.main()

