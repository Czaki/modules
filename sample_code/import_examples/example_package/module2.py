"""
This module show import and usage functions from same level module and package
"""

from .module1 import module1_function1
from .example_subpackage1 import submodule1_function2


def module2_function1():
    print("[module2.module2_function1] execute")
    module1_function1()
    submodule1_function2()
