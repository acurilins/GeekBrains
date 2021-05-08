import sys


my_file = "lesson_5.1.txt"

try:
    with open(my_file, 'r') as fh:
        lines = [line for line in fh.readlines() if line != '\n']
except IOError as e:
    print(e)
    sys.exit(1)

print(f'There are {len(lines)} lines in the file.')

for line in lines:
    print(f'Line {line[:50]} consists of {len(line.split())} word(s)')
