# Python errors

error: AttributeError: 'module' object has no attribute 'ArgumentParser'
reason: Usually this symptom is the result of shadowing a builtin module with one of your own

error: ValueError: Attempted relative import in non-package 
reason:
      File "parse_csv_test.py", line 2, in <module>
        from ..src.parse_csv import read_data
    ValueError: Attempted relative import in non-package
http://stackoverflow.com/questions/11536764/how-to-fix-attempted-relative-import-in-non-package-even-with-init-py/27876800#27876800


exception types:
ValueError 
OSError 
ImportError
TypeError
NameError
AttributeError
IOError





