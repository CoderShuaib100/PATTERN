# creating the algorithm
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of cols: "))
items = str(input("Enter a string that you want to add as the pattern item like '*', '%' , '/': "))


# creating the loop (nested loop)
for i in range(1 , rows + 1):
    for j in range(1 , cols + 1):
        print(items,end=" ")
    print()