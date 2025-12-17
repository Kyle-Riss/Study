def solution(num_list):
    
    mul_res = 1
    for n in num_list:
        mul_res *= n
    
    sum_res = sum(num_list) ** 2
    
    if mul_res < sum_res:
        return 1
    else: 
        return 0