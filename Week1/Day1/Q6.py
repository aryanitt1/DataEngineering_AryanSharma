a = 5
b = 7
print(f"a = {a}")
print(f"b = {b}")
print()

c = a 
print(f"Memory Location of a = {id(a)}")
print(f"Memory Location of c = {id(c)}")
#Memory Location of a and c are both same.
print()

d = b
print(f"b = {b}")
print(f"d = {d}")
print(f"Memory Location of b = {id(b)}")
print(f"Memory Location of d = {id(d)}")

b = 9
print()
print("After changing reference of b to object 9--")   
print(f"Memory Location of b = {id(b)}")
print(f"Memory Location of d = {id(d)}")
#d still pointing to the earlier reference while b is changed

list1 = [1 , 2 , 3 , 4]
list2 = list1
print(f"list1 = {list1}")
print(f"list2 = {list2}")

print("After appending 5 to list 1")
list1.append(5)
print(f"list1 = {list1}")
print(f"list2 = {list2}")
#Effected to both
print()

print(f"Memory Location of list1 = {id(list1)}")
print(f"Memory Location of list2 = {id(list2)}")
#To avoid this we can use list2 = list1.copy()
print()
x = 10
print(f"Current address of x reference = {id(x)}")
x = x + 1
print(f"Address of x reference after incrementing x by 1 = {id(x)}")
