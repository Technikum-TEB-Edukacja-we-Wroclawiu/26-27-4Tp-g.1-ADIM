with open('plik.txt', 'r') as plik:
    odczyt = plik.read()

# Z ilu wersów składa się wiersz?
odczyt = odczyt.split('\n')
print(len(odczyt))