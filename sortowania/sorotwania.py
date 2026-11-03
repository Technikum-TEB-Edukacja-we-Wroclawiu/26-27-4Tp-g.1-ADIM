import random


def druga_najwieksza(liczby: list[int]) -> int:
    # max = liczby[0]
    # for liczba in liczby:
    #     if liczba > max:
    #         max = liczba
    maksimum = max(liczby)

    nowe_liczby = []
    for liczba in liczby:
        if liczba < maksimum:
            nowe_liczby.append(liczba)

    max2 = nowe_liczby[0]
    for liczba in nowe_liczby:
        if liczba > max2:
            max2 = liczba

    return max2


# print(druga_najwieksza([1, 3, 2, 7, 5, 7]))
# druga_najwieksza(1)

def buble_sort(liczby: list[int]) -> list[int]:
    for i in range(len(liczby)):
        for j in range(i + 1, len(liczby)):
            if liczby[i] > liczby[j]:
                liczby[i], liczby[j] = liczby[j], liczby[i]

    return liczby


losowa_lista = [random.randint(1, 100) for _ in range(20)]


# print(buble_sort(losowa_lista))

# print(sorted(losowa_lista))

def selection_sort(liczby: list[int]) -> list[int]:
    for i in range(len(liczby)):
        min_index = i
        for j in range(i + 1, len(liczby)):
            if liczby[j] < liczby[min_index]:
                min_index = j
        liczby[min_index], liczby[i] = liczby[i], liczby[min_index]

    return liczby


print(selection_sort(losowa_lista))
