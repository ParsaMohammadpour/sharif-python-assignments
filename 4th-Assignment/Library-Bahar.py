class Library:
    pass
import json
data_dictionary = json.loads(input())
lib = Library()
for i in data_dictionary.keys():
    if data_dictionary[i] != 0:
        setattr(lib, i, data_dictionary[i])
command = ''
while command != 'end':
    command = input().split()
    if command[0] == 'add':
        if hasattr(lib, command[1]):
            setattr(lib, command[1], getattr(lib, command[1]) + int(command[2]))
        else:
            setattr(lib, command[1], int(command[2]))
    elif command[0] == 'print':
        if hasattr(lib, command[1]):
            print(getattr(lib, command[1]))
        else:
            print(0)
    elif command[0] == 'have':
        print(hasattr(lib, command[1]))
    elif command[0] == 'delete':
        if hasattr(lib, command[1]):
            delattr(lib, command[1])
    elif command[0] == 'borrow':
        if hasattr(lib, command[1]):
            if getattr(lib, command[1]) == 0:
                delattr(lib, command[1])
            else:
                setattr(lib, command[1], getattr(lib, command[1]) - 1)
                if getattr(lib, command[1]) == 0:
                    delattr(lib, command[1])
    elif command[0] == 'end':
        break
    else:
        print('command not found')