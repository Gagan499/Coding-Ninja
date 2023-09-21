n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == 1:
            print(1, end='')
        elif j == 1 or j == i:       # 1 and i are position in row   #j == 1 to print first element in each row   
            print(i - 1, end='')          #AND     j == i       to print last element in each row
        else:
            print(0, end='')
    print()
