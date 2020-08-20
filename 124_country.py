def solution(num):
    answer = ""
    
    while num:
        num, nam = divmod(num, 3) 
        # divmod num: num 나누기 3의 몫, nam: num 나누기 3의 나머지
        print(num, nam)
        
        answer = "사일이"[nam] + answer
        print(answer)
        
        if not nam: # 나머지가 0일때 num에 1을 뺀다
            num -= 1
            
    return answer


solution(15)

