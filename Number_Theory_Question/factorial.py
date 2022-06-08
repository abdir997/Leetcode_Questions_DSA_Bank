


def getFactorial(n):
    ans = 1
    count = 0
    for i in range(1,n+1): #1,2,3,4
        ans = ans * i # 1*1, 2*1, 3*2, 4*6
        count += 1 #1,2,3,4
    return ans # 24


