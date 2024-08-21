def fib(n): #write a Fibonacci up to n
    a,b = 0, 1
    while a < n:
        print(a,end=' ')
        a,b = b, a + b
fib(2000)
#assign function
f = fib

f(100)

print(f(0)) #return as None