import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import pyfile_info

def test_classes_functions():
    funcs, classes = pyfile_info.get_file_info("SamplePackage/test/afile.py")
    assert len(classes) == 1
    assert len(funcs) == 2
    assert classes == ['Class1']
    assert funcs == ['function1', 'function2']

