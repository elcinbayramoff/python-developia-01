a = "python"
b = a.replace("y", "n")
print(b)  # pnthon, birinci daxil edilən stringi tapır və ikinci ilə əvəz edir.

#/////////////////////////////////////////////////////////////////////////////////////

a = "python"
b = a.upper()
print(b)  # PYTHON, bütün hərfləri böyük edir.

#/////////////////////////////////////////////////////////////////////////////////////

a = "PYTHON"
b = a.lower()
print(b)  # python, bütün hərfləri kiçik edir.

#/////////////////////////////////////////////////////////////////////////////////////

a = "pythooon"
b = a.count("o")
print(b)  # 3, daxil edilən ifadənin neçə dəfə baş verdiyini qaytarır

#/////////////////////////////////////////////////////////////////////////////////////

a = "python is very easy"

b = a.title()

print(b) # Python Is Very Easy, Hər sözün ilk hərfini böyük hərf edir

# #/////////////////////////////////////////////////////////////////////////////////////

a = "python is very easy"

b = a.istitle()

print(b) # False, Hər sözün böyük hərflə başladığını yoxlayır