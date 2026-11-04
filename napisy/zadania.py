def logowanie(login:str, haslo: str) -> None:
    proby = 3
    login = login.lower()
    while proby > 0:
        wpisany_login = input('Podaj login: ')
        wpisane_haslo = input('Podaj haslo: ')
        wpisany_login = wpisany_login.lower()
        if haslo == wpisane_haslo and login == wpisany_login:
            print('Zalogowano')
            return
        else:
            print('błędny login lub hasło')
            proby -= 1
    print('Zablokowano!')


#logowanie('adam', '1234')


def zadanie15(tekst: str, slowo: str) -> None:
    index = tekst.find(slowo)
    dlugosc = len(slowo)
    wystapienia = 0
    indeksy = []
    while index != -1:
        #print(tekst[index:dlugosc+index])
        wystapienia += 1
        print(index)
        indeksy.append(index)
        index = tekst.find(slowo, index+dlugosc)

    print(f'Liczba wystąpień: {wystapienia}')
    nowy_tekst = ""
    aktualny = 0
    for i in range (len(tekst)):
        if i == indeksy[aktualny]:
            nowy_tekst += "["+tekst[i]
        elif i == indeksy[aktualny] + dlugosc:
            nowy_tekst += "]"+tekst[i]
            if aktualny < len(indeksy) + 1:
                aktualny += 1
        else:
            nowy_tekst += tekst[i]

    print(nowy_tekst)



zadanie15('Ala ma kot. Kot ma Ale', 'Al')


def zadanie12(wiadomosc:str, zakazane: list[str]) -> str:
    oryginalny = wiadomosc
    wiadomosc = " " + wiadomosc.lower()
    for slowo in zakazane:
        wiadomosc = wiadomosc.replace(' '+slowo.lower()+' ', ' '+'*'*len(slowo)+' ')
        wiadomosc = wiadomosc.replace(' '+slowo.lower()+'.', ' '+'*'*len(slowo)+'.')
        wiadomosc = wiadomosc.replace(' ' + slowo.lower() + ',', ' ' + '*' * len(slowo) + ',')


    # naprawa
    wiadomosc = list(wiadomosc)
    wiadomosc = wiadomosc[1:]
    for i in range(len(wiadomosc)):
        if wiadomosc[i] != '*' and wiadomosc[i] != oryginalny[i]:
            wiadomosc[i] = oryginalny[i]

    return "".join(wiadomosc)

print(zadanie12('Ala ma kot. Kot Ma Ale', ['Al', 'kot']))
