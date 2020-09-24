"""
This file is sample script which use ``example_package``
"""

from example_package.example_subpackage1.submodule2 import (
    submodule2_function1 as pkg1_submodule2_function1,
)
from example_package import pkg2_submodule2_function1
from example_package.module2 import module2_function1


if __name__ == "__main__":
    print("=" * 20)
    pkg1_submodule2_function1()
    print("=" * 20)
    pkg2_submodule2_function1()
    print("=" * 20)
    module2_function1()
