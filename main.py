import sys


def initialization():
    sys.path.insert(1, 'util')
    import project_reader
    
    project_path = askdirectory(title='Select Folder') # shows dialog box and return the path
    return project_path

def main():
    project_path = initialization()
    