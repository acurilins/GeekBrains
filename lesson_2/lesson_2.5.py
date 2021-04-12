a = [7, 5, 3, 3, 2]
additional = int(input('Enter additional number: '))
i = 0

for n in a:
    if additional <= n:
        i = i + 1
a.insert(i, additional)
print(a)