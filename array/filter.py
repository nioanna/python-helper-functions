#Ova funkacija prihvata niz celih brojeva i ispisuje niz parnih celih brojeva
def filterEvenArray(arr):
    for item in arr:
        if(item%2==0):
            print(item)
#Ova funckija ispisuje sve neparne elemente niza 
def filterOddArray(arr):
    for item in arr:
        if(item%2!=0):
            print(item)

#Ova funkcija ispisuje sve brojeve koji su veci u odnosu na zadati broj 
#Kao parametre prihvata niz celih broja i ceo broj 

def filterBiggerThenNum(arr, num):
    for item in arr:
        if(item>num):
            print(item)
#
filterEvenArray([1,2,3,4]); 
print("----------------------------")
filterOddArray([1,2,3,4]);
print("----------------------------")
filterBiggerThenNum([1,2,3,4,5], 3);