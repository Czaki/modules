"""
This module presents usage ``as`` for rename imported element
adn import elements from other subpackage
"""

from .submodule1 import submodule1_function1 as local_submodule1_function1
from ..example_subpackage1.submodule1 import submodule1_function1, submodule1_function2


def submodule2_function1():
    print("[example_submodule2.submodule2.submodule2_function1] execute")
    local_submodule1_function1()
    submodule1_function2()
    submodule1_function1()
