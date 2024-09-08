# Capitalize metodu --------------------

word1 = "python"
new_word1 = word1.capitalize()
print(new_word1)

# Python, stringin ilk simvolunu boyuk yazir.


# Upper metodu --------------------

word2 = "html"
new_word2 = word2.upper()
print(new_word2)

# HTML, stringin butun herflerini boyuk yazir.


# Lower metodu --------------------

word3 = "CSS"
new_word3 = word3.lower()
print(new_word3)

# css, stringin butun herflerini kicik yazir.


# Title metodu --------------------

word4 = "java script"
new_word4 = word4.title()
print(new_word4)

# Java Script, stringde her sozun ilk herfi boyuk yazilir.


# Swapcase metodu --------------------

word5 = "Jquery"
new_word5 = word5.swapcase()
print(new_word5)

# jQUERY, stringin boyuk herflerini kicik, kicik herflerini boyuk yazir.


# Find or index metodu --------------------

word6 = "Visual studio"
new_word6 = word6.find("studio")
print(new_word6)

# 7, stringden verilen ifadenin indexini yazir.


# Rindex or rfind metodu --------------------

word7 = "Scratch"
new_word7 = word7.rindex("t")
print(new_word7)

# 4, stringe sagdan baslayib ifadenin ilk indexini yazir.


# Replace metodu --------------------

word8 = "Bootstrap"
new_word8 = word8.replace("o", "A")
print(new_word8)

# BAAtstrap, stringden birinci verilen ifadeni ikinci ile deyisir.


# Length metodu --------------------

word9 = "Java"
new_word9 = len(word9)
print(new_word9)

# 4, stringin uzunlugunu tapir.


# Count metodu --------------------

word10 = "Pandas"
new_word10 = word10.count("a")
print(new_word10)

# 2, stringde ifadenin sayini tapir.


# Lstrip metodu --------------------

word11 = " React "
new_word11 = word11.lstrip()
print(new_word11)

# React_, soldaki bosluqlari silir.


# Rstrip metodu --------------------

word12 = " C++ "
new_word12 = word12.rstrip()
print(new_word12)

# _C++, sagdaki bosluqlari silir.


# Strip metodu --------------------

word13 = " SCSS "
new_word13 = word13.strip()
print(new_word13)

# SCSS, soldaki ve sagdaki bosluqlari silir.


# Split metodu --------------------

word14 = " Cyber Security "
new_word14 = word14.split()
print(new_word14)

# ['Cyber', 'Security'], bosluqla ayrilmis list olur.


# Join metodu --------------------

word15 = " / "
new_word15 = word15.join("Kotlin")
print(new_word15)

# K / o / t / l / i / n, butun herflerin ortasina evvelki element qosulur.