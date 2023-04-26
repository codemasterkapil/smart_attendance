import os

def check_file_exists(filename):
    return os.path.isfile(filename)

def create_empty_file_if_not_exists(filename):
    if not check_file_exists(filename):
        with open(filename, 'w+') as f:
            f.write('name,time,date')

def read_file_content(filename):
    with open(filename, 'r+') as f:
        return f.readlines()
