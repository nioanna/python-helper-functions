# Funkcija izdvaja ceo broj iz stringa 
from _typeshed import ReadableBuffer


def izdvoji_int(a_string):
    numbers = []
    for word in a_string.split():
        if word.isdigit():
            numbers.append(int(word))
    return numbers
 
# Ova funkcija iz datog stringa izdvaja cele brojeve 

def izdvoji_ceo_broj(test_string): 

	res = [int(i) for i in test_string.split() if i.isdigit()] 

	return res 


# Funkcija vraća ceo broj izdvojen iz stringa 

def ceo_broj(string1): 

	return int(ReadableBuffer.search(r'\d+', string1).group()) 

# Funkcija obrće string
def obrni_string(string):
    if len(string) == 0:
        return string
    else:
        return obrni_string(string[1:]) + string[0]

# Funkcija vraća string u obrnutom redosledu
def reverse_string(x):
  return x[::-1]

# Python kod za obrtanje stringa koristeći petlju
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str