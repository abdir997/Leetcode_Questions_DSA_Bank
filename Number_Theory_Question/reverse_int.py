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


def reverse_int(x):  # 123 -> 321
    list = []  # 3
    count = 0
    flag = 0  # flag = 0 - no is positve ,  flag =1 , number is nagative

    if x < 0:  # -20
        x = -1 * x  # making positve = -1 * -20 = 20
        flag = 1
        res = 0
        while x > 0:  #20 
            digit = x % 10  # 3 , 2
            count = digit  # 2
            list.append(digit)
            res = sum(d * 10 ** x for (x, d) in enumerate(list[::-1]))
            x = x // 10  # 12


            if flag == 1:  # negvaitve
                res = -1 * res  # negative
                if res < -2 ** 31 or res > 2 ** 31 - 1:
                    return 0
                return res

            if res < -2 ** 31 or res > 2 ** 31 - 1:
                return 0
            return res

print(reverse_int(-1234))

