import os

def list_ext_files(loc, extension)
    extfiles = []
    flist = os.listdir(loc)
    for fl in flist:
        fext = path.splitext(fl)[0]
        if fext == extension:
            extfiles.append(fl)
    return extfiles
