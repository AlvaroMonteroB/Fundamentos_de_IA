import csv


def read_file(path):
    with open(path,'r') as f:
        lectura=csv.reader(f)
        f.close()
    return lectura

def write_file(path,data):
    with open(path,'w') as f:
        f.write(data)
        f.close()

