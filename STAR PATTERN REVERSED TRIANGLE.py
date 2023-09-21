
n=int(input())
for i in range (n):
    k=(input())
    k=int(k)
    for j in range (k):
        print(" "*j,end="")
        print("*" *(k-j),end="")
        print()