def find_smallest_integer_divisor(numb):
    n = 2
    while n > 1:
        if numb % n == 0:
            return(n)
        else:
            n += 1

print(find_smallest_integer_divisor(15))