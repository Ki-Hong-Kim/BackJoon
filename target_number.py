def solution(numbers, target):
    sup= [0] # 0을 넣는 이유:
             # 빈 리스트를 
    
    for i in numbers:

        result = [] # 초기화
        
        for j in sup : 
            
            
            result.append(j+i) # 더하고 뺀값을 결과에 넣고
            result.append(j-i)
            
            
        print(len(result), "4 번")
        
        sup = result # 조합의 결과를 저장하는 곳
        print(result)
    return sup.count(target)

solution([5, 6, 8, 9], 6)





####################
# dfs
answer = 0
def DFS(idx, numbers, target, value):
    # numbers와 target은 고정이고 idx와 value만 변함
    global answer
    N = len(numbers)
    
    if(idx == N and target == value):
        # idx == N을 충족해야 하는 이유:
        # 입력된 숫자를 모두 사용한 경우에서 타겟숫자와 같은 결과를 counting 하기 때문
        answer += 1
        return
    
    if(idx == N):
        return
    
    DFS(idx+1, numbers, target, value+numbers[idx])
    DFS(idx+1, numbers, target, value-numbers[idx])

def solution2(numbers, target):
    global answer
    DFS(0,numbers,target,0)
    
    return answer

solution2([5, 6, 8, 9], 6)

##############################
# bfs
import collections

stack = collections.deque([(0, 0)])
a = []
while stack:
    a.append("3")
    print(a)
    if len(a) == 3:
        stack = False
    
    
    
    
    
    
    
    
def solution3(numbers, target):
    answer = 0
    stack = collections.deque([(0, 0)])
    while stack:
        current_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((current_sum+number, num_idx + 1))
            stack.append((current_sum-number, num_idx + 1))

    return answer

solution3([1, 2, 3, 4, 5], 3)








