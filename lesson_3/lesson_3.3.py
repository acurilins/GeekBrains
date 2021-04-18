def my_func(x, y, z):
    my_list = [x, y, z]
    return sum(sorted(my_list)[1:])


print(my_func(20, 11, 30))
