translation = {'One': 'Viens', 'Two': 'Divi', 'Three': 'Tris', 'Four': 'Cetri', 'Five': 'Pieci'}
"""Русский заменен на латышский"""
my_list = []
result = []
try:
    file_obj = open("lesson_5.4.txt", 'r')
    for line in file_obj:
        numbers = line.split(" - ")
        if numbers[0] in translation:
            word = translation[numbers[0]]
            result.append(word + ' - ' + numbers[1])
    print(result)
except IOError:
    print("Error!")
finally:
    file_obj.close()

try:
    new_file = open("lesson_5.4.amended.txt", "w")
    new_file.writelines(result)
except IOError:
    print("Error!")
finally:
    new_file.close()
