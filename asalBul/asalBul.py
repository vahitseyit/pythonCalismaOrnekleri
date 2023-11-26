
sayi = int(input('Bir sayi giriniz \n'))
for i in range(2, sayi + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
                print(i)

