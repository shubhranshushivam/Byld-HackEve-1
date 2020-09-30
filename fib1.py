from functools import lru_cache

@lru_cache(maxsize=1000)
def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n>2:
        return fib(n-1)+fib(n-2)


n = int(input("Enter the number of times you want to input n :"))
for i in range (0,n+1):
	print (fib(i))
