def operation(*args):
    #четные числа
    even = []
    for arg in args:
        if arg % 2 == 0:
            even.append(arg)
    odd = []
    #нечетные числа
    for arg in args:
        if arg % 2 != 0:
            odd.append(arg)
    return even, odd,

qqq = operation(2, 4, 6, 3, 5, 7, 10, 12, 11, 13, 14)
print(qqq)
