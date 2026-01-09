a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("Before Swap-")
print(f"   First Number  : {a}")
print(f"   Second Number : {b}")

a = a ^ b
b = a ^ b
a = a ^ b

print("After Swap")
print(f"   First Number  : {a}")
print(f"   Second Number : {b}")    