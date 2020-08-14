# [14502]laboratory

# 입력 데이터
# 1. 행렬 구조(x, y)
# 2. 각 행에 입력될 값 = 0: 빈공간, 1: 벽, 2: 바이러스 출발점

# 출력 데이터
# 행렬에 벽 3개를 추가로 생성하고 바이러스가 다 퍼졌을때 남은 최대 안전지역 수

# 문제 이해
# 벽 3개를 세울수 있는 모든 경우의 수에서 각 경우의 수의 안전지역 수를 확인하고
# 그 중 가장 많은 안전지역 수를 선택

# 우리가 알아야 하는 값은 안전지역 수이다.
# 반대로 바이러스 감염된 지역 수를 알면 안전 지역 수를 알 수 있다.

# 왜? 우리는 행렬 구조를 알고 있어서 전체 구역의 개수(n*m)를 알고 있고
# 벽의 개수는 고정되어 있기 때문에
# 안전 구역 수 = (전체 구역 수 - 벽의 개수) - 바이러스 퍼진 구역 수

# 따라서 바이러스 퍼진 구역 수가 가장 작을 때 안전 구역 수가 가장 클때 라는 것을 알 수 있다.
# 문제에서 가장 중요한 것: 추가 될 3개의 벽의 위치!!!

# 3중 for문에 마지막 for문에는 재귀함수가!!


# 기본 입력 데이터들
n, m = 7, 7
#n, m = map(int, input().split()) # x축, y축
board = [[2, 0, 0, 0, 1, 1, 0],
         [0, 0, 1, 0, 1, 2, 0],
         [0, 1, 1, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0]]

#board = [list(map(int, input().split())) for _ in range(n)] # 행렬데이터
visited = [[False] * m for _ in range(n)] # 방문여부 확인용 행렬

virus = [] # 바이러스 좌표 확인용 빈 list
num_virus = 9999 # 바이러스 퍼진 구역 수를 최소값으로 업데이트 하기위한 vector임. 최소 (n * m) 보다 크기만 하면됨
safe = -3  # 벽을 3개 꼭 세워야함.

###### 3 ######
# 세워진 3개의 벽에서 감염지역 수 찾기
def dfs(x, y):  # virus를 퍼뜨린다.
    res = 1
    visited[x][y] = True
    
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):  # 위, 아래, 좌, 우
        nx, ny = x + dx, y + dy
    
        if nx < 0 or nx >= n or ny < 0 or ny >= m:  # 맵의 경계보다 커진다면
            continue                                # 넘어간다.
        if not (visited[nx][ny] or board[nx][ny]):  # 방문하지 않았거나, 벽(1)이 아니라면
            res += dfs(nx, ny)                      # board[nx][ny] 때문에 바이러스가 인접해도 괜찮음
            
    return res # 감염이 퍼진 칸 수


###### 2_0 ######
# 3개 벽을 세우는 모든 경우의 수를 통해 최소 바이러스 감염지역 수 찾는 과정
def solve(start, wall):  # 벽을 세운다 (start = 0, wall = 0)
    
    global n, m, num_virus, visited # n, m은 행렬 값
                                    # num_virus = 계속 업데이트 되는 바이러스 구역 최소 값(초기값: 9999)
                                    # visited = 방문여부 확인 테이블
                                    # global은 전역변수 지정으로 함수내에서 적용하면 앞서 설정한 값도 변경된다.
    ###### 2_2 ######
    if wall == 3:  # 벽이 3개라면
        count = 0
        visited = [[False] * m for _ in range(n)] # 추가된 벽 3개의 위치가 바뀔때마다 초기화
        for x, y in virus: # virus : 바이러스 좌표를 갖고있는 리스트
            count += dfs(x, y)
            
        num_virus = min(num_virus, count) # num_virus는 최소값이 나올때마다 업데이트 됨
        print("wall = ", wall, "\n")
        
        return 

    ###### 2_1 ######
    # 추가로 벽 세우는 작업
    for i in range(start, n * m): # range(strat, end) ==> 처음 부터 끝까지 
        
        # 2차원 배열에서 x, y의 조합을 뽑습니다.(이해 중요)
        x = i // m     # 몫 0 / n == 0
                       #    n / 0 불가능
        y = int(i % m) # 나머지 

        if board[x][y] == 0: # 빈칸(0) 이라면/ 0이 아니라면 다음 좌표로 넘어감
            board[x][y] = 1  # 벽(1)을 세운다
            print("i = ", i, "x= ", x, "y = ", y, "wall = ", wall)
            
            solve(i + 1, wall + 1) # 2_1 --> 2_0 로 이동
            
            # wall == 3 됐을때 return 위치 여기부터 시작하고 for 시작
            board[x][y] = 0  # 위에서 세운 벽을 다시 빈칸(0)으로 만든다. (초기화) // 조건을 충족하지 않을 때를 생각하면 두번쨰 벽을 이해 할 수 있음
            


###### 1 ######
# 아직 벽 3개를 추가하지 않은 행렬에 대한 작업
for i in range(n): # 행
    for j in range(m): # 열

        if board[i][j] != 1:  # 벽이 아니라면,
            safe += 1         # safe는 전체 구역에서 벽의 개수만 제외한 값
                              # 맨 위에 보면 safe가 -3으로 시작 하는데 나중에 추가될 벽을 미리 계산해둔 값임
            
        if board[i][j] == 2:  # virus라면
            virus.append((i, j)) # 좌표 저장

###### 2 ######
#import sys
#sys.stdout = open('output.txt','w')
 
solve(0, 0)
print(safe - num_virus)

'''
벽이 세워지는 위치에 대한 원리
m = 5
# 첫번째 벽
for i in range(1, 9):
    x = i // m
    y = i % m
    print(x, y)

    # 두번째 벽
    for i in range(2, 9):
        x = i // m
        y = i % m
        print(x, y)
        
        # 세번째 벽
        for i in range(3, 9):
            x = i // m
            y = i % m
            print(x, y)
'''  
'''
for i in range(30, 49):
    x = i // m     # 몫 0 / n == 0
                       #    n / 0 불가능
    y = int(i % m) # 나머지    
    print(x, y)
'''