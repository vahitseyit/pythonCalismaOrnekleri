def asllariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)


sayi1 = int(input("sayi 1: "))
sayi2 = int(input("sayi 2: "))
if sayi1 > sayi2:
    bos = sayi2
    sayi2 = sayi1
    sayi1 = bos



asllariBul(sayi1, sayi2)
