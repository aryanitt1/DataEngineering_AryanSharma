import gc
# in python everything is an object (variable , list , function, string , etc).
# When a variable is created, it creates memory of memory for it and then stores object in memory.
# The variable name points/references to that object


x = 5
#here an object is created which is 5 and x stores the reference of it.

y = 7
z = y

#both z and y will point to the object 7 or store the reference of it
#reference count for the object 7 is 2 currently as 2 variables are referring to it or pointing to it

del y #deallocation
#It will decrement the reference count and only z will point to obj 7 now, but obj 7 will still exist

del z 
#It will decrement the reference count to 0 and now obj 7 will also deallocated

list1 = [1 , 2 , 3]
list2 = list1

list1.append(4)
print(list2)  #It is priting [1,2,3,4] since both were reffering to same memory

gc.collect() #Cleans cyclic garbage is present