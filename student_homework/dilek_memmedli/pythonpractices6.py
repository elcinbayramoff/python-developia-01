# set={1,2,3,2}
# print(set)
# #dublikata icaze verilmir



# a=set([1,2,3])
# print(a)


# a={1,2,3,4}
# for i in a:
#     print(i)

# if 2 in a:
#     print(True)



# set={1,2,3}
# say=len(set)
# print(say)


# a={1,2,3}
# a.add(4)
# print(a)
#1element elave etmek ucundur



# a={1,2,3,4}
# a.update([5,6])
# print(a)
#list,tuple,dict,str elave edir



a={1,2,3}
# a.remove(2)
# print(a)
#verilmis elementi silir,yoxdursa error qaytarir

# a.discard(3)
# print(a)
#verilmis elementi silir,error qaytarmir

# a.pop()
# print(a)
#random silir

# a.clear()
# print(a)
#setin icini bosaldir



a={1,2,3}
b={4,5,6}

# c=a.union(b)
# print(c)
# print(a)
#esas seti deyismir

# a.update(b)
# print(a)
#esas seti deyisir



a={3,8}
b={1,2,3}
# c=a.intersection(b)
# print(c)
#ortaqlari qaytarir esas set deyismir

# a.intersection_update(b)
# print(a)
#esas set deyisir


# c=a.symmetric_difference(b)
# print(c)
#ortaq olmayanlari qaytarir,esas set deyismir

a.symmetric_difference_update(b)
print(a)














