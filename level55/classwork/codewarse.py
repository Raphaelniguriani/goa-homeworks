def small_enough(array, limit):
    num = 0
    for i in array:
        if i >= limit:
            num += 1
    if num > 0:
        return False
    else:
        return True
 