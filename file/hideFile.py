import os

# Ova funkcija sakriva dokument za UNIX sisteme, tako sto dodaje tacku na pocetak fajla
def hideUnixFile(path, fileName):
    os.rename(path+'/'+fileName, path+'/.'+fileName)

# Ova funkcija sakriva dokument za Windows sisteme, tako sto postavlja attribut na hidden
def hideWindowsFile(path, fileName):
    fn = path+fileName
    p = os.popen('attrib +h ' + fn)
    t = p.read()
    p.close()
