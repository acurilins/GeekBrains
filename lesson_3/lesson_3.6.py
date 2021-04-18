def int_func(latin):
    allowable = 'abcdefghijklmnopqrstuvwxyz'
    if set(latin).difference(allowable):
        False
    else:
        return latin.title()


words = input('Введите строку из слов разделенных пробелами ').split()
for w in words:
    result = int_func(w)
    if result:
        print(int_func(w), ' ')
