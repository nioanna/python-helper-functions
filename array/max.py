# Funkcija trazi najvecu vrednost niza
def max(array):
    maxValue = array[0]
    for item in array:
        if item > maxValue:
            maxValue = item
    return maxValue

print(max([40, 30, 1, -20, 30, -6]))


