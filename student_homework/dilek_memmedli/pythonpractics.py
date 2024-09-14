a="developia"
b="engineering"
c="academy"
x=a+" "+b+" "+c
print(x)

a=6
b=14
c=a+b
print(c)

a=6
b=-14
c=a+b
print(c)

a=6
b=4
c=a-b
print(c)

a=2
b=3
c=a*b
print(c)

a=2
b=3
c=a**b
print(c)

a=10
b=3
c=a%b
print(c)


a=3
a+=2
print(a)

b=6
b-=2
print(b)

a=20
a//=10
print(a)

a=50
b=10
a*=b
print(a)


a=-8
print(abs(a))

a=8
print(int(a))

a=8.0
print(int(a))

a=8.4
print(int(a))

a=[1,2,3,4,5]
print(max(a))
print(min(a))

import math
a=16
print(math.sqrt(a))


import math
a=25
print(math.sqrt(a))

import math
a=4
print(math.exp(a))

import math
a=4.7
print(math.floor(a))
print(math.ceil(a))

import math
a=-4.6
print(math.floor(a))
print(math.ceil(a))

a="ironman"
print(a)

a="ironman"
b=a[ : ]
print(b)

a="ironman"
b=a[ :3]+"x"+a[4: ]
print(b)

a="ironman"
b=a[0:4]
print(b)

a="iron"
b="man"
c=a+" "+b
x=a+b
print(c)
print(x)

a="man"
b=f'iron{a}'
print(b)

a="\"asus\""
print(a)

a="ironman"
b=a.capitalize()
print(b)


a="ironman"
b=a.upper()
print(b)

a="IRONMAN"
b=a.lower()
print(b)

a="iron man"
b=a.title()
print(b)

a="iRonMaN"
b=a.swapcase()
print(b)

a="  ironman  "
print(a.lstrip())
print(a.rstrip())
print(a.strip())
print(a.split())


a="ironman"
b="*"
print(b.join(a))

a="ironman"
b="%"
print(b.join(a))

a="ironman"
print(a.isalpha())

a="7"
print(a.isalpha())

a="6"
print(a.isdigit())

a="4"
print(a.isalnum())

a="ironman"
print(a.isalnum())

a="ironman"
print(a.isupper())

a="IRONMAN"
print(a.islower())


a="ironman"
b="n"
print(a.find(b))

a="hello worl"
b="worl"
print(a.find(b))

a="ironman"
b="n"
print(a.index(b))

a="ironman"
b="r"
print(a.rindex(b))

a="ironman"
b="r"
c="x"
print(a.rfind(b))
print(a.rfind(c))
print(a.rindex(b))


a="ironman"
b=a.replace("n","x")
print(b) 

 
a="ironman"
b=a.count("o")
print(b)

a="iron\nman"
print(a)

a="iron\tman"
print(a)

a="iron\\man"
print(a)


a="man"
b=f'iron{a}'
print(b)

a=["hulk","deadpool","doctor strange"]
print(len(a))

a="hulkdeadpool"
b="hulk,deadpool"
print(list(a))
print(list(b))

a=["hulk","deadpool"]
print(len(a))


a=["ironman","hulk","vision","thor","loki"]
print(list(a[ : ]))
print(list(a[ :3]))
print(list(a[2: ]))

a=["captan amerika","wanda"]
a[0]=["groot"]
print(a)

a=["groot","venom","loki","vision"]
a[0:2]=["hulk"]
print(a)

a=["1","2","3","4"]
a.insert(2,"5")
print(a)
a.append("5")
print(a)
a.extend(["10","11"])
print(a)
a=a+["12","13"]
print(a)

a=["1","2","3"]
a.remove("3")
print(a)

a=["1","2","3"]
a.pop(1)
print(a)

a=[5,4,3,2,1]
a.sort()
print(a)

a=[1,2,3]
a.reverse()
print(a)

'''lesson4'''

'''task1'''
a=[4,2,1,5,7,3,6,8]
a.sort()
print(a)
a1=a[2:6]
print(a1)
a1.reverse()
print(a1)
a2=a[ :2]+a1+a[6: ]
print(a2)


'''task3'''
a=[2,1,2]
a.reverse()
print(a)

a=[1,3,4,3,1]
b=a
print(b)
a.reverse()
print(a)

a=[7,8,9,8,7]
b=a
print(b)
a.reverse()
print(a)

'''task4'''
a=[1,2,3]
b=a[2]
c=a[1]
d=a[0]
print(b)
print(c)
print(d)
print("[",b,",",c,",",d,",","]")












