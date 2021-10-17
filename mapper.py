import sys
from numpy import mat, mean, var

def read_file(file_path):
    for i in file_path:
        yield i.rstrip()

input_mas = [float(i) for i in read_file(sys.stdin)]
print('%d\t%f\t%f' % (len(input_mas), mean(mat(input_mas)), var(input_mas)))