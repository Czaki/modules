"""
this is __init__ file of example_package package
"""

from example_package.example_subpackage2.submodule2 import (
    submodule2_function1 as pkg2_submodule2_function1,
)

from .module2 import module2_function1


__all__ = ("pkg2_submodule2_function1", "module2_function1")
