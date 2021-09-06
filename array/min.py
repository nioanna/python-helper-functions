# Funkcija trazi najmanju vrednost niza
def min(array):
    minValue = array[0]
    for item in array:
        if item < minValue:
            minValue = item
    return minValue

# print(min([40, 30, 1, -20, 30, -6]))