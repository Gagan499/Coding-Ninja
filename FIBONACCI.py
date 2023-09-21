n=int(input())
def Fibonacci(n):
    if(n==0 or n==1):
        return n
    else:
        return Fibonacci(n-2)+Fibonacci(n-1)
print(Fibonacci(n))