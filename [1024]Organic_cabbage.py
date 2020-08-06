# 참고 BackJoon 에서는 외부 라이브러리(ex numpy, pandas ...) 사용에 제한

import sys
sys.setrecursionlimit(50000) 
# 재귀제한높이설정
# python3 에서는 재귀함수제한의 기본값이 1000으로 넓혀줘야함

dx = [-1, 0, 1, 0] # dx와 dy는 같이 봐야함
dy = [0, 1, 0, -1] # index를 통해 묶이며 (x, y)를 4방향으로 움직이기 위한 값


######  3_1  ######
def dfs(x, y):
    matrix[x][y]= 0 # 배추가 심어져있는 곳은 0으로 바꾸는 이유
                    # 이동 할때 왔던 곳을 다시 가지 않게 하기 위함
    
    for i in range(4): # 4방향으로 움직이기 위한 for 문
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 배추 밭의 범위를 넘어가면 지나친다
        if nx<0 or nx>=m or ny<0 or ny>=n:
            continue
        
        # 이동 했을 때 배추가 심어져있다면 4방향으로 움직이는 함수 한번 더 실행
        if matrix[nx][ny] == 1:
            dfs(nx,ny)


######   2   ######            
def solve():
    cnt = 0
    
    for i in range(m):
        for j in range(n):
            
            if matrix[i][j] == 1:
                dfs(i,j)
                
                ### 3_2 ###
                cnt += 1 # 인접한 부분이 끝나면 cnt가 1씩 늘어남
                         # cnt = 필요한 배추흰지렁이 수
    print(cnt)
                

######  1  ######
t = int(input()) # 테스트 케이스 입력

for _ in range(t): # 따로 받을 값이 없이 반복하는 작업만 필요하므로 _를 사용
    
    # 참고 데이터 입력 속도 stdin.readline() >>> input()
    m, n, k = list(map(int, sys.stdin.readline().split())) # M: 가로길이 N: 세로길이 K: 배추 개수
    
    # 입력된 값으로 배추밭 틀 만드는 작업
    matrix = [[0] * n for _ in range(m)]
    
    
    # 빈 배추밭에 배추 심는 작업
    for _ in range(k):
        
        link = list(map(int, input().split()))
        
        matrix[link[0]][link[1]] = 1
        
    solve() # 최종으로 cnt가 출력됨
    
    