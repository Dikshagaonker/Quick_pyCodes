"""
Fibonacci number series :
Starts with 0 and 1 as first two numbers in series .
The rule of fibonacci is we add first two numbers to get third
number.

"""


"USING GENERATOR RANGE"

def fibonacci(num):
    a = 0
    b = 1
    for i in range (num):
        yield a
        temp = a
        a = b
        b = temp + b
        
        
for item in fibonacci(20):
    print (item)


"USING LIST"

def fib(num):
    a = 0
    b = 1
    result = [ ]
    for i in range (num):
        result.append (a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib(20))
        
