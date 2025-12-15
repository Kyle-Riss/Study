def solution(a, b):
    val1 = int(str(a) + str(b))
    val2 = 2 * a * b
    
    if val1 >= val2:
        return val1
    else:   
        return val2