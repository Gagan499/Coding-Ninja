N=int(input())

for row in range (N):         #row+1 as row start from zero 
    for col in range(row+1):
        print("*",end="")
    print()    