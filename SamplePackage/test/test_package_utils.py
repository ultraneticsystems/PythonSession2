import pytest
import sys, os
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import package_utilities


def test_python_files():
    loc = os.getcwd()
    extfiles = package_utilities.list_ext_files(loc, '.py')
    packagelist = ['setup.py']
    assert len(extfiles) == len(packagelist) and sorted(extfiles) == sorted(packagelist)

def test_noexist_files(capsys):
    loc = os.getcwd()
    extfiles = package_utilities.list_ext_files(loc, '.nonense_ext_3_14159265359')
    out, err = capsys.readouterr()
    assert len(extfiles) == 0
    assert "\n no files with extension " in out
    
