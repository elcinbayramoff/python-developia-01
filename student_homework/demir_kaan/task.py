#capitalize metodu

text = "salam dostum"
print(text.capitalize())

#Bir setird yalnızca ilk hərfi böyük hərfə çevirir və qalan hərfləri kiçik hərfə çevirir. 

#casefold metodu

text = "SALAM DOSTUM"
ae = text.casefold()
print(ae)

# Setirdəki bütün hərfləri kiçik herflere çevirmek üçün istifadə olunur.

#center metodu

text = "Salam"
ae = text.center(10)
print(ae)

#setiri ortalayır və boşluqları simvollarla doldurur.


#count metodu

text = "Hello, Hello , Hello"
H = text.count("Hello")
print(H)

#bir simvolun neçe defe tekrarlandığını sayma üçün istifade olunur


#encode metodu 
#baxtım biraz garışıx geldi başa düşmedim tam olarax

#exbandtabs metodu

text = "Salam\tDemir"
D = text.expandtabs(13)
print(D)

#tab simvollarını(/t) seçdiyimiz uzunluqdaki boşluqlarla evez edir


#find metodu

text = "Men Demir"
ae = text.find("mir")
print(ae)

#bir simvolun yerleştiği ilk indexi tapır


#format metodu

text = "Salam {} Necesen"
ae = text.format("Demir")
print(ae)

#setirde müeyyen edilmiş deyerleri ekrana çıxardır


#index metodu

text = "Salam Demir"
ae = text.index(" Demir")
print(ae)

#simvolun yerleştiyi ilk indexi tapır


#isalnum metodu 
text1 = "Demir2008"
text2 = "Demir 2008"
text3 = "2008"
text4 = "Demir£2008"
print(text1.isalnum())  
print(text2.isalnum())  
print(text3.isalnum()) 
print(text4.isalnum())

#setirdeki bütün simvollar alfasayısaldırsa true gaytarır


#isalnum metodu

text1 = "Demir"
text2 = "Demir456"
text3 = "128689"
text4 = "Demir@"

print(text1.isalpha())  
print(text2.isalpha())  
print(text3.isalpha())  
print(text4.isalpha())

#bütün simvolların elifba herfleri olduğunu yoxlayır


#isdecimal metodu

text1 = "644223"
text2 = "65634dd"

print(text1.isdecimal()) 
print(text2.isdecimal()) 

#bütün simvolların regem olduğunu yoxluyur



#islower metodu

text1 = "salam Demir"
text2 = "salam demir"

print(text1.islower())  
print(text2.islower())  
 
#setirdaki herflerin kiçik herfle yazıldığını yoxlayır


#ljust metodu

text = "ddddd"
ae = text.ljust(19, '-')
print(text)

#setiri soldan dolduraraq genişlendirir


#lower metodu

text = "SALAM DEMİR"
ae = text.lower()
print(ae)
#setirdeki bütün herfleri kiçik herflere çevirir







