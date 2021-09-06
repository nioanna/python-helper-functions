# Pronalazi indeks elementa u nizu
def findIndex(array, value):
    index=0
    for item in array:
        if item == value:
            return index
        index = index + 1
    return -1

print(findIndex([1,3,4,5], 1))