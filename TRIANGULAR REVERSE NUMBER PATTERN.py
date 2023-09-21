N = int(input())
for i in range(1, N + 1):
    for j in range(i, 0, -1):     #starting from i, going down to 1, with a step of -1
        print(j, end='')
    print()

#-1 is the step value. It decrements j by 1 in each iteration, effectively counting down