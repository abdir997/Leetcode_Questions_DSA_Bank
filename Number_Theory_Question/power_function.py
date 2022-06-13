import re


def pow(x,n):
    res = 1
    for i in range(1,n+1):#O(N)
        res = res*x
    return res

x=3
n=5
print(pow(x,n))



def powOptimize(x,n):
    half = n//2

    halfPower = pow(x,half)

    if n%2 == 0:
        return halfPower * halfPower
    else:
        return halfPower * halfPower * x

x = 3
n = 5
print(powOptimize(x,n)) 
