"""
This module show different way to import functions from module from same package.
All these functions are implemented in ``submodule1.py`` file.

import of ``submodule1_function2`` and ``submodule1_function4``
base on imprort this function to ``__init__.py``

"""

from example_package.example_subpackage1.submodule1 import submodule1_function3
from example_package.example_subpackage1 import submodule1_function4

from .submodule1 import submodule1_function1
from . import submodule1_function2


def submodule2_function1():
    print("[example_submodule2.submodule1.submodule2_function1] execute")
    submodule1_function1()
    submodule1_function2()
    submodule1_function3()
    submodule1_function4()
