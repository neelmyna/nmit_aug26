import pdb

pdb.set_trace()

def partition_array(diameters):
    pivot = diameters[-1]
    k = 0
    for i in range(len(diameters)-1):
        if diameters[i] < pivot:
            diameters[k], diameters[i] = diameters[i], diameters[k]
            k += 1
    diameters[k], diameters[-1] = diameters[-1], diameters[k]    


input_size = int(input("Enter sie of the Array: "))

diameters = list() # []
print(f'Enter diameters of {input_size} Oranges: ')
for i in range(input_size):
    diameter = int(input())
    diameters.append(diameter)

partition_array(diameters)

print(f'Array after partition is ', diameters)

    
    