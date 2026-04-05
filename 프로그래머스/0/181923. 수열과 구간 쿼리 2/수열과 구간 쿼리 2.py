def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        target_list = []
        
        for i in range(s, e + 1):
            if arr[i] > k:
                target_list.append(arr[i])
        
        if not target_list:
            answer.append(-1)
        else:
            answer.append(min(target_list))
            
    return answer