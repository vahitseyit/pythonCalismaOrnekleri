


def tamBolenBul(sayi):
    tamBolenler = []

    for i in range(1, sayi + 1):
        if sayi % (i) == 0:
            tamBolenler.append(i)
    return tamBolenler


sayi = int(input('Bir sayi giriniz: '))

print(tamBolenBul(sayi))

