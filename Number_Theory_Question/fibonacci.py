
def fibonaaci(n):
    list = [0,1]
    for i in range(2,n):
        next_term = list[-1]+list[-2]
        list.append(next_term)

    return list


print(fibonaaci(5))