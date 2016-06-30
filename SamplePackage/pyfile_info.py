

def get_file_info(src):
    fp = open(src, 'r')
    functions = []
    classes = []
    for ln in fp:
        if 'def ' in ln:
            parts = ln.split()
            functions.append((parts[1].split('('))[0])
        elif 'class ' in ln:
            parts = ln.split()
            classes.append((parts[1].split('('))[0])
    return [functions, classes]
