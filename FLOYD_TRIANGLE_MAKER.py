h = int(input("Enter the height: "))
num = 0 
for i in range(1,h + 1):
    for j in range(1,i + 1):

        num = num + 1
        print(num,end=" ")
    print()