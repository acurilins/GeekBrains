def task_4(x, y):
    try:
        z = x ** y
    except TypeError:
        return "Wrong input"
    return z


print(task_4(2, 3))

