



############ 아래와 내용은 같음 for문을 한줄로 썻는지 아닌지만 다름
def solution(skill, skill_trees):
    cnt = 0
    for case in skill_trees :
        a = [case.index(i) for i in skill if i in case]        
        
        a_ = sorted(a)
        if a == a_ and all(i in case for i in skill[:len(a)]): cnt+=1
    return cnt


################ 이해하긴함
def solution(skill, skill_trees):
    cnt = 0
    for case in skill_trees :
        
        a = [] # 스킬트리의 조건부 스킬의 인덱스를 저장
        
        for i in skill: # 선행 스킬 순서대로 있는지 조사
            if i in case:
                a.append(case.index(i)) # 스킬의 위치를 저장
        
        print(a, "길이", len(a)) 
                 # 조건부 스킬 위치의 인덱스를 저장 (조건부 스킬이 들어간 개수)
                 # 
        
        
        a_ = sorted(a) # 조건을 만족하는지 확인하기 위해 생성
        
        
        print(all(i in case for i in skill[:len(a)]))
        
        if a == a_ and all(i in case for i in skill[:len(a)]):
            # a == a_ 선행스킬의 조건을 만족
            # and
            # all(i in case for i in skill[:len(a)])
            # 선행스킬이 case에 있어야한다. == skill의 처음부터 a의 길이 까지 있어야 한다.
            
            cnt+=1
            
    return cnt

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "CD"])


def solution(skill, skill_trees):
    answer = 0
    
    for case in skill_trees:
        a = []
        
        for i in skill:
            if i in case:
                a.append(case.index(i))
        
        a_sorted = sorted(a)
        
        if a == a_sorted and all(i in case for i in skill[:len(a)]):
            answer += 1

    return answer