import sys
import ast


with open("lootbag.txt", "r") as f:
    input_string = f.read()
    if len(input_string) > 0:
        bag = ast.literal_eval(input_string)
    else:
        bag ={}
    if sys.argv[1] == 'add':
        if sys.argv[2] not in bag:
            bag[sys.argv[2]] = []
        bag[sys.argv[3]].append(sys.argv[2])
    elif sys.argv[1] == 'remove':  
        bag[sys.argv[3]].remove(sys.argv[2])
    elif sys.argv[1] == 'ls':
        if len(sys.argv) == 2:
            for key in bag.keys():
                print(key)
        elif len(sys.argv) == 3:
            for toy in bag[sys.argv[2]]:
                print(f'{toy}')

with open("lootbag.txt", "w") as f:
    f.write(str(bag))




        


# print(bag)