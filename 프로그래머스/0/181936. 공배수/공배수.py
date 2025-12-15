def solution(number, n, m):
    
    is_multiple = (number % n == 0) and (number % m == 0)

    return 1 if is_multiple else 0