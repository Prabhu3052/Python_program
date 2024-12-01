n =   int(input("Enter:"))
e=0
for i in range(n):
    for j in range(i,n-1):
        print("0",end=" ")
    print(n-i)
