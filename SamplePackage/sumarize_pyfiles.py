from __future__ import print_function
import os
import os.path as path
import sys
import pyfile_info as finfo
import package_utilities as utils

class PyFileSummary(object):
    def __init__(self, loc):
        self.location = loc
        self.pyfiles = []
        self.classes = []
        self.functions = []

    def find_pyfiles(self):
        self.pyfiles = utils.list_ext_files(self.location, '.py')

    def get_file_info(self):
        for fl in self.pyfiles:
            fpath = path.join(self.loc,fl)
            fclasses, ffunctions = finifo.checkfile(fpath)
            self.classes.extend(fclasses)
            self.functions.extend(ffunctions)
            
    def summarize(self):
        text1 = "\n " + loc " contains " + str(len(self.pyfiles))
        text1 += " python files,"
        text2 = str(len(self.classes)) + " python classes and "
        text3 = str(len(self.functions)) + " functions or methods."
        print(text1)
        print(text2)
        print(text3)
        print("files: ", self.pyfiles)
        print("classes: ", self.classes)
        print("functions: ", self.functions)

def main(argv):
    """
    doc string
    """
    fsum = PyFileSummary(argv[0])
    fsum.find_pyfiles()
    fsum.get_file_info()
    fsum.sumarize()


if __name__ == "__main__":
    main(sys.argv)
