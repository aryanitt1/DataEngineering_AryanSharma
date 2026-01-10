size = int(input("Enter size of pyramid required: "))

for i in range (0 , size):
    for j in range (0 , size - i - 1):
        print(" " , end = "")
    for k in range(0 , 2 * i + 1):
        print("*" , end = "")
    print("")