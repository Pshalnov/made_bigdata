import sys

result_size = 0
result_mean = 0
result_var = 0

for i in sys.stdin:
    i = i.strip()
    buff, mean, var = i.split('\t')

    result_var = (result_size * result_var + buff * var) / (result_size + buff) + result_size * buff * ((result_mean - mean) / (result_size + buff)) ** 2
    result_mean = (result_size * result_mean + buff * mean) / (result_size + buff)
    result_size += buff

print('%f\t%f' % result_mean, result_var)