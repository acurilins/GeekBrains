initial = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [initial[a] for a in range(1, len(initial)) if initial[a] > initial[a - 1]]
print(new_list)

