"""
This module is for show example of running package as code
"""

from .module1 import module1_function1
from .example_subpackage1 import submodule1_function2


def module3_function1():
    print("[module3.module3_function1] execute")
    module1_function1()
    submodule1_function2()


if __name__ == "__main__":
    print("[main execute]")
    module3_function1()
