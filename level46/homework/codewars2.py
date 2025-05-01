def digitize(n):
    list = []
    n = str(n)
    for i in n:
        list.append(int(i))
        
    return list[::-1]