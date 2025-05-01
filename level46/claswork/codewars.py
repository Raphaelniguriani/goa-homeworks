def repeats(arr):
    result = []
    for i in arr:
        if arr.count(i) == 1:
            result.append(i)
             
    final_result = sum(result)  
    return final_result
    pass

