#Ova funkacija prihvata niz celih brojeva i ispisuje niz parnih celih brojeva
def filterArray(arr):
    for item in arr:
        if(item%2==0):
            print(item)

filterArray([1,2,3,4]); 