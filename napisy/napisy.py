text = "  Ala ma kota, a kot ma Ale!  "

print(len(text))
print('\n Zmiana wielkości liter')
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.upper())
print(text.swapcase())

print('\n Usuwanie spacji')
print(text.strip())
print(text.lstrip())
print(text.rstrip())

print('\n Zmiana fragmentu')
print(text.replace('kota', 'psa'))
print(text.replace('kot', 'pies'))
print(text.replace(' ', ''))


print('\n Wyszukiwania')
print(text.find('kot'))
print(text.count('kot'))
print('kot' in text)
print(text.startswith('kot'))
print(text.endswith(' '))

print('\n Indeksowanie')
print(text[3:5])
print(text[:5])
print(text[2:])
print(text[::2])
print(text[::-1])

print('\n Dzielnie napisu')
text = "jabłko,gruszka,banan"
splited = text.split()
print(splited)
print(",".join(splited))

print('\n Sprawdzanie zawarotości')
print('1234'.isdigit())
print('1234'.isalpha())
print('PYthon1234'.isalnum())
print("\n    ".isspace())
print("abc".islower())
print("ABC".isupper())

print(ord('a'))
print(chr(97))