"""
Some broken buggy code
"""
import os
import os.path as path
import sys

def average_number_of_lines(loc):
    """
    compute the average number of lines of python code in a directory
    """
    flist = os.listdir(loc)
    npyfiles = 0
    nlines = 0
    for fl in flist:
        fext = path.splitext(fl)[0]
        if fext == '.py':
            npyfiles += 1
            fp = open(fl,'r')
            for ln in fp:
                nlines += 1
    avelines = nlines/npyfiles
    return avelines

def main(argv):
    """
    doc string
    """
    avelines = average_number_of_lines(argv[1])
    print avelines


if __name__ == "__main__":
    main(sys.argv)
