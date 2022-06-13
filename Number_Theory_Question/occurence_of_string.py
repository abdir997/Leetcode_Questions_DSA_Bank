def getCount(s,t):

    counter = 0

    for i in s:
        if i == t: #iterates through whole string and only counts when i==t
            counter+=1

    return counter

s = 'acdaaddbc'
t = 'c'
print(getCount(s,t))


def getCount1(s,t):
    counter = 0

    for i in range(len(s)):# enhcnaed for loop # 0, len(s)-1
        if s[i] == t:
            counter+=1
    return counter

s = 'acdaaddbc'
t = 'c'
print(getCount1(s,t))