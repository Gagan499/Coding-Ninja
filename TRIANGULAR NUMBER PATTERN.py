N=int(input())

for row in range (N):
    for col in range(row+1):
        print(row+1,end="")                #row+1 as row start from zero 
    print()    