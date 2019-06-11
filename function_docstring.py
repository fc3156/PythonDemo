def print_max(x, y):
    '''prints the maximum of two numbers.打印两个数值中的最大数。



    the two values must be integers.这两个数都应该是整数
    '''
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maxmum')
    else:
        print(y, 'is maxmum')


help(print_max)
print_max(3, 5)
print(print_max.__doc__)
