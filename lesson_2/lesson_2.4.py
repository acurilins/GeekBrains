a = input('Enter words separated with space: ').split()

for i, word in enumerate(a, 1):
    if len(word) <= 10:
        print(i, word)
    else:
        print(i, word[:10])