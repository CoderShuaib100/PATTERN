# creating the algorithm
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
for i in range(1,rows + 1):
    for j in range(1,cols + 1):
        if(i == 1 or i == rows or j == 1 or j == cols or i == j):
            print(" * ",end="")
        else:
            print("   ",end="")
    print()