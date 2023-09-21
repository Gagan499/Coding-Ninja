n=int(input())
reverse=0
k=n
while(k>0):
    lastdigit =int(k%10)
    reverse=reverse*10+lastdigit
    k=k//10

if(n==reverse):
    print("true")
else:
    print("false")