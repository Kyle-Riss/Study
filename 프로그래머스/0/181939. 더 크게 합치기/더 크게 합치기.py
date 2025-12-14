def solution(a, b):
    val1 = int(str(a) + str(b))
    val2 = int(str(b) + str(a))
    
    answer = max(val1, val2)
    return answer