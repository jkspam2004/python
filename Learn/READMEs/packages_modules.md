* A Python module is simply a Python source file, which can expose classes, functions and global variables.
** When imported from another Python source file, the file name is treated as a namespace.

* A Python package is simply a directory of Python module(s).
    __init__.py : this file tells Python to treat this directory as a package


A module is a single Python source file (or files) that are imported under one import and used.
    import my_module

A package is a collection of modules in directories that give a package hierarchy.
    from my_package.timing.danger.internets import function_of_love



-m mod : run library module as a script
python -m tdd_package.test.parse_csv_test


http://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py/27876800#27876800

~/Git/python/Learn/tdd_package/src/parse_csv.py
                            ../test/parse_csv_test.py

1. importing module with relative path:
if __name__ == '__main__':
    print "package:", __package__

    if __package__ is None:
        """
        1a. run inside of test dir: test$ python parse_csv_test.py
        """
        import sys
        sys.path.insert(0, "../src")

        try:
            from parse_csv import read_data
            sys.path.pop(0)
        except ImportError:
            print('No Import')
    else:
        """
        1b. run outside of tdd_package dir: Learn$ python -m tdd_package.test.parse_csv_test
        """
        from ..src.parse_csv import read_data

2. importing module with absolute path:
# first export PYTHONPATH to parent directory of package
$ echo PYTHONPATH=~/Git/python/Learn
from tdd_package.src.parse_csv import read_data
