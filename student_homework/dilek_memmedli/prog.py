a="dilek"
b=a[1:3]
print(b)

a="dilek"
b=a[:2]+"b"
print(b)

yas=17
x=f"dileyin yasi {yas}dir"
print(x)

ad="dilek"
soyad="memmedli"
x=ad+" "+soyad
print(x)


x="she's a student"
print(x)

x="memmedli"
y=x[ :6]+"zade"
print(y)

x="informatika"
y=x[ :7]+"siya"
print(y)

a="azerbaycan"
b=a.capitalize()
print(b)
'''sozun ilk herfini boyuk yazir'''

a="azerbaycan"
b=a.upper()
print(b)
'''butun herfleri boyuk yazir'''

a="AZERBAYCAN"
b=a.lower()
print(b)
'''BUTUN HERFLER KICIK YAZILIR'''

a="azerbaycan respublikasi"
b=a.title()
print(b)
'''sozun ilk herfi boyuk yazilir'''

a="AzErBaYcAn"
b=a.swapcase()
print(b)
'''kicik herf boyuk , boyuk herf kicik yazilir'''

a="azerbaycan olkedir"
b=a.find("olkedir")
print(b)
'''sozun indexinin necenci oldugunu gosterir'''


a="azerbaycan olkedir"
b=a.index("olkedir")
print(b)
'''findla eyni alindi'''

a="zeher"
b=a.replace("z","s")
print(b)
'''evez etdi'''

a="dilek memmedli"
print(len(a))

a="dilek"
b=a.len()
print(b)


a="memmedli"
b=a.count(a)
print(b)