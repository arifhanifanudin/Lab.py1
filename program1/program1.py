# Menentukan Nilai Terbesar Dari 3 Bilangan
def pengulangan():
    print ('masukkan 3 bilangan')
    a=int(input('bilangan a = '))
    b=int(input('bilangan b = '))
    c=int(input('bilangan c = '))

    if a>b :
        if a>c:
            print (a, 'terbesar')
        else:
            print (c, 'terbesar')
    elif b>c :
        if b>c:
            print (b, 'terbesar')
        else:
            print (c, 'terbesar')

    print ('')

pengulangan()


