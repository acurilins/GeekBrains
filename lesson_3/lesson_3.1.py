def div(x, y):
    try:
        x, y = int(x), int(y)
        result = x / y
    except ZeroDivisionError:
        return "Can't divide by zero"
    return round(result)


print(div(input('Input first number - '), input('Input second number - ')))
