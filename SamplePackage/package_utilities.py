import os
import os.path as path

def list_ext_files(loc, extension):
    extfiles = []
    flist = os.listdir(loc)
    for fl in flist:
        fext = path.splitext(fl)[1]
        if fext == extension:
            extfiles.append(fl)
    if len(extfiles) == 0:
        line = "\n no files with extension " + extension + " found in " + loc
        print line
    return extfiles
