*******
Modules
*******

Code organization
=================

It is easier to found something in code
if code is organized in short functions 
and this functions are grouped in some logical way
(For example one group for reading data, 
second for perform calculation and third for prepare summary).

The most common way is to keep such groups in separated files 
or if codebase is bigger then in separated directories.

As all common language Python support this. 
In Python such organized units are called modules and packages. 

Documentation: https://docs.python.org/3/tutorial/modules.html

Understand import
+++++++++++++++++

Lets have file ``sample_module.py`` with content

.. code-block:: python

    def hello_world():
        print("Hello world")

If user run python shell inside same directory as
file ``sample_module.py`` is saved then fou could use it 
in two way

.. code-block:: python
    
    import sample_module

    sample_module.hello_world()

and 

.. code-block:: python
    
    from sample_module import hello_world

    hello_world()

The first one need more characters for
call buts provide explicit information from which module 
function is called. It is useful if code use more 
than one module with same named function

Second one produce shorter code and its nice 
when writing single task script or in jupyter notebooks.

Assume that ``sample_module`` growth enough to split it on multiple 
files, but we do not want to need to fix import
in our previous scripts. Then this code could be organized in package. 

But import inside package use different syntax.

.. code-block:: python

    from sample_module import sub_module

or

.. code-block:: python

    from . import sub_module

of course package elements could be modules or packages. 
Bellow there is structure of ``example_package`` from ``sample_code/import_examples``

.. code-block::

    .
    ├── example_package
    │   ├── __init__.py
    │   ├── example_subpackage1
    │   │   ├── __init__.py
    │   │   ├── submodule1.py
    │   │   └── submodule2.py
    │   ├── example_subpackage2
    │   │   ├── __init__.py
    │   │   ├── submodule1.py
    │   │   └── submodule2.py
    │   ├── module1.py
    │   └── module2.py
    └── sample_script.py

Exercises
=========

Exercise 1
++++++++++
Read code from ``sample_code/import_examples`` and check if you understand all constructions used in it. 

Exercise 2
++++++++++
Create project which will calculate base statistics of of ``data/iris.csv`` 
Which will calculate basic statistics (``mean``, ``median`` and ``std``) of each column. 
Project structure should be:

.. code-block::

    ├── iris_analysis
    │   ├── __init__.py
    │   ├── io
    │   │   ├── __init__.py
    │   │   ├── load.py
    │   │   └── save.py
    │   └── calculate.py
    └── run_analysis.py


Code Organization Problems
++++++++++++++++++++++++++
This section describe typical problems
which user could meet when work with
code split on separate files and possible
strategies to solve its.

Circular import 
~~~~~~~~~~~~~~~
The problem 

Call file form package using path
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Do not call file which is inside package providing path to it. 

.. code-block:: bash

    $ python path/to/file.py

It will fail if its used any relative import.
Use approach presented in `Calling code from package/module`_

Name collision with existing library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Python search for module to load is similar for shell searching 
for executable. This list could be obtain from ``sys.path`` variable. 
Byt default it contains script directory and some set of path
from Python interpreter installation. It could be extended
from Python code or using ``PYTHONPATH`` environment variable. 
This is very powerful mechanism, but there is possibility that 
pearson witting code use same name for his own top level package/module
as package already installed, even builtin one. 
Sample of such situation could be found in 
``sample_code/path_pollution_example``. 

So if after some unrelated changes part of code
starts failing with ``AttributeError`` or 
``ImportError`` then check if some of
new files [#git_reason]_ does not collide with some of python package installed in you environment. 


Calling code from package/module
++++++++++++++++++++++++++++++++

There are scenario where some code from function or module could be called as separated program.
Because of import mechanism in Python calling its using path to file is a bad idea. 

Beside simple solution of creating wrapping script. Ex:

.. code-block:: python 
    
    from example_package.module1 import submodule1_function1

    submodule1_function1()

there is option to use ``-m`` flag (PEP 338):

.. code-block:: bash

    $ python -m example_package.module1

Running same code on import (side effect) is bad practice. 
There is special variable ``__name__``. 
If module is run as script its value is ``"__main__"``. 

Because of this all code which should be executed only if using module as script 
such be put under such clause:

.. code-block:: python

    if __name__ == "__main__":
        run_code()

Additional exercises
====================

Exercise 3
++++++++++
Solve circular dependencies problem in ``circular_import1`` using delayed import.

Exercise 4
++++++++++
Solve circular dependencies problem in ``circular_import2`` by export problematic functions to additional module.


.. [#git_reason] History of changes could be checked using VCS (like GIT). Next reason to use version control system.