# printer
from collections import deque

def solution(priorities, location):
    answer = 0
    problem = deque(priorities)
    sample = deque([0] * len(priorities))
    sample[location] = 1
    
    while max(sample) == 1:
        if problem[0] == max(problem):
            problem.popleft()
            sample.popleft()
            answer += 1
        
        else:
            problem.append(problem.popleft())
            sample.append(sample.popleft())

    return answer


priorities =  [1, 2, 3, 4, 5, 4, 3, 5] 
pi_list = [(p, i) for i, p in enumerate(priorities)]
for i, item in enumerate(priorities):
    print(i, item)
pr = pi_list.pop(0)
pr[0]
p_list = [priority for priority, idx in pi_list]

for i, item in enumerate(priorities):
        print(i, item)

def solution2(priorities, location):
           #입력데이터:
            #중요도를 저장한 리스트, 출력할 문서의 위치
            # 출력할 문서가 몇번째로 출력될지 고민해야
     pi_list = [(p, i) for i, p in enumerate(priorities)] 
     # 중요도를 리스트 안에 중요값과 인덱스로 나눠 저장한다
     waiting_q = [] # 나중

     while pi_list:
         pi = pi_list.pop(0) # 첫번째 출력물에 대한 정보
         priority = pi[0]    # 첫번째 출력물의 중요도
         
         p_list = [priority for priority, idx in pi_list] # 첫번째 출력물을 제외한 
                                                          # 나머지 출력물의 중요도만 저장한 리스트
         
         if p_list:
            max_p = max(p_list) # 지금 출력 위치에 있는 출력물보다
                                # 높은 값이 있나 확인하기 위한 값
 
         if priority >= max_p:   # 첫 출력물이 나머지 출력물 중 가장 큰 값보다 크다면
            waiting_q.append(pi) # waiting_q에 저장(pi는 중요도와 인덱스값이 저장되어있음)
         
         else: # 나머지 출력물중 더 큰게 있다면 뒤로감
            pi_list.append(pi)
 
     for i, item in enumerate(waiting_q):
        if item[1] == location:
            return i + 1

######################
def solution(priorities, location):
     pi_list = [(p, i) for i, p in enumerate(priorities)] # (중요도, 인덱스) 형식으로 저장
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
             return i + 1, waiting_q

##
i, test = solution([2, 1, 3, 2], 2)
for i, item in enumerate(test):
    print(i, item)

#####################
def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans
