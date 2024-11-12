import random
can=3
puan=0
x=random.randint(0,2)

oyun=['tas','kagit','makas']

while (can!=0):
    x=random.randint(0,2)
    bilgisayarhamle=oyun[x]
    hamle=input('tas,kagit,makas:\n')
    if bilgisayarhamle==hamle:
        print('berabere')
    elif hamle=='tas':
        if bilgisayarhamle=='kagit':
            can-=1
            print('kaybetdiniz',can,'caniniz kaldi')
        else:
            puan+=10
            print('tebrikler! 10 puan kazandiniz')
    elif hamle=='kagit':
        if bilgisayarhamle=='makas':
            can-=1
            print('kaybettiniz',can,'caniniz kaldi!')
        else:
            puan+=10
            print('tebrikler!!10 puan qazandiniz')
    elif hamle=='makas':
        if bilgisayarhamle=='tas':
            can-=1
            print('kaybettiniz',can,'caniniz qaldi')
        else:
            puan+=10
            print('tebrikler! 10 puan qazandiz')
print('oyun bitdi')
print(puan)
    
            



