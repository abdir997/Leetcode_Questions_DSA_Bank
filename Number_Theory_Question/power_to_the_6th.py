from re import I


def getValue(n):
    i = 0
    while True:
        if(i==n**6):
            return i 
        i+=1


def getValue1(n):
    i=0
    ans = 1
    while True: # O(6) = O(1)
        if i==6:
            return ans
        ans = ans *n # 64 # 2**6 = 2*2*2*2*2*2
        i+=1 
        
# O(n**6)
