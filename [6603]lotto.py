from itertools import combinations # 조합을 구해야하므로 cobinations를 사용해야함

# 몇개가 입력될지 모르니 while을 써야함
flag = True # flag를 조건문으로 사용해 flag가 False로 변하기 전까지 while 작동

while flag:
    line = list(map(int, input().split())) # 선택한 번호의 수와 번호들이 들어온다
    
    n = int(line[0]) # 첫번째 숫자는 종료를 위한 조건문으로만 사용됨
    
    if n == 0: # 첫번째 숫자가 0일때 종료
        flag = False # while 종료 조건으로 바꾸고
        break # 반복문 탈출
    
    for case in combinations(line[1:], 6): # 입력된 데이터의 2번째 숫자부터 끝까지 사용하는데 
                                           # 6개 숫자로 이뤄진 조합을 구함
        
        print(' '.join(map(str, case))) # 출력 양식: 각 숫자를 한칸씩 띄어서 출력
        
    print('\n') # 조건문이 입력될때 한줄씩 띄어야함
        
    