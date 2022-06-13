def getSum(n):
    sum = 0
    while n>0:
        digit = n%10
        sum = sum + n
        n= n//10
    return sum

