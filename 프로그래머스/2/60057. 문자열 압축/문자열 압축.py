def solution(s):
    if len(s) == 1:
        return 1
    
    n = len(s)
    answer = n  # 초기값을 문자열의 길이로 설정

    def check_compact(x):
        compressed_len = 0
        count = 1
        prev = s[:x]
        
        for i in range(x, n, x):
            curr = s[i:i+x]
            if prev == curr:
                count += 1
            else:
                compressed_len += len(str(count)) if count > 1 else 0
                compressed_len += len(prev)
                prev = curr
                count = 1
        
        compressed_len += len(str(count)) if count > 1 else 0
        compressed_len += len(prev)
        
        return compressed_len

    for i in range(1, n//2 + 1):
        answer = min(answer, check_compact(i))
    
    return answer