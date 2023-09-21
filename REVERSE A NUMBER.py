N=int(input())
reverse=0
while(N>0):
    lastdigit =int(N%10)
    if lastdigit!=0:
        reverse=reverse*10+lastdigit
    N=N//10
print(reverse)    
