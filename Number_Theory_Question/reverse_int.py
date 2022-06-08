# algorithm 
# 1. seperate the digit # 145 % 10 --> 5 
# 2. 14 % 10 --> 4
# 3. 14//10 = 4
# 4. 4%10 --> 4
# 5. 4//10 --> 0


''''

def getSum(n): # 145 = 1 + 4 + 5 = 10
    sum =0 
    while n>0:
      digit = n%10 # 5 , 4
      sum = sum+digit 0 +5 , 5 + 4, 9 +1
       n = n//10    14, 1,0

return sum  10

'''

from unicodedata import digit


def reverse_int(n): #123 -> 321
    list = [] #3
    count = 0
    while n>0: #123
        digit = n%10 # 3 , 2
        count = digit #2
        list.append(digit)
        n = n//10 #12
    return list

print(reverse_int(123))
