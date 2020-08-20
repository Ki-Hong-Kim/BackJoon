# printer
# 런타임 오류 발생
# 원본1
def solution(priorities, location):
    answer = 0
    
    sample = [0] * len(priorities)
    sample[location] = 1
    
    while max(sample) == 1:
        if priorities[0] == max(priorities):
            priorities.pop(0)
            sample.pop(0)
            answer += 1
        
        else:
            priorities.append(priorities.pop(0))
            sample.append(sample.pop(0))

    return answer

# 테스트
def solution(priorities, location):
    answer = 0 # 출력 순위
    sample = [0] * len(priorities) 
    sample[location] = 1 # 출력할 문서 용
    
    while max(sample) == 1: # 출력할 문서가 출력되면 중단
        if priorities[0] == max(priorities):
            priorities.pop(0)
            sample.pop(0)
            answer += 1
        
        else:
            priorities.append(priorities.pop(0))
            sample.append(sample.pop(0))
        
        print("테스트", answer, "\n",priorities,'\n',sample)

    return answer

priorities =  [1, 2, 3, 4, 5, 4, 3, 5] 
priorities[5]
solution([1, 2, 3, 4, 5, 4, 3, 5], 5)



######################이해함
def solution(priorities, location):
     pi_list = [(p, i) for i, p in enumerate(priorities)]  # enumerate는 중요도의 인덱스까지 출력해주는 함수
     # (중요도 p, 인덱스 i) 형식으로 저장
     waiting_q = []

     while pi_list: # pi_list에 내용이 없어질때까지 반복
         pi = pi_list.pop(0) # pi_list 첫번째 값을 뺌(중요도, 인덱스)
         priority = pi[0] # 중요도
         p_list = [priority for priority, idx in pi_list] 
         # 첫번째 값을 제외한 나머지 문서의 중요도만 가져와서 리스트로 저장
         
         if p_list: 
             max_p = max(p_list) # 나머지 리스트 중 가장 높은 중요도를 저장

         if priority >= max_p: # 첫번째 문서의 중요도와 나머지 문서중 가장 높은 중요도를 비교
             waiting_q.append(pi) # 첫번째가 더 높으면 waiting_q에 첫번째 문서(중요도, 인덱스)를 저장
         
         else: # 나머지 문서중 중요도가 더 높은게 있다면
             pi_list.append(pi) # 첫번째 문서의 내용을 맨 뒤로 보냄
             # pi는 중요도와 인덱스 값을 갖고 있음

     for i, item in enumerate(waiting_q): # waiting_q는 실제 출력 순서를 저장한 값
         # i 가 인덱스, item이 중요도
         if item[1] == location:
             return i + 1

##
i, test = solution([2, 1, 3, 2], 2)
for i, item in enumerate(test):
    print(i, item)

##################### 이해함
def solution(p, l): # p는 문서별 중요도가 적힌 리스트 / l: 출력 순위가 궁금한 문서의 위치
    ans = 0 # 원하는 문서가 출력된 순위
    m = max(p)
    
    while True:
        v = p.pop(0) # 맨 앞에 있는 중요도를 뺌
        
        if m == v: # 맨 앞 문서의 중요도가 max값일때
            ans += 1 # 일단 출력됨
            
            if l == 0:  # 첫 출력시 맨 앞 문서의 중요도가 가장 높고 궁금했던 문서가 맨 앞 문서라면 종료
                break
            
            else: # 첫 출력시 맨 앞 문서의 중요도가 가장 높지만 궁금한 문서가 아닐경우
                l -= 1 # 궁금한 문서가 앞당겨짐
            
            m = max(p) # 중요도의 max값이 바뀜
        
        else: # 맨 앞 문서의 중요도가 max가 아닐때
            p.append(v) # 맨 뒤로감
            if l == 0: # 맨 앞문서가 궁금한 문서일 경우
                l = len(p)-1 # 궁금한 문서의 위치를 맨 뒤로 보냄
            
            else: # 아닐경우 앞문서가 뒤로 가므로 
                l -= 1 # 궁금한 문서는 앞으로 당겨짐
    return ans
