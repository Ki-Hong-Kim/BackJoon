# [2468] 안전영역
import sys
sys.setrecursionlimit(100000)

###### 2_1 ######
def dfs(x, y, z): # x, y == 좌표 / z 강수량
    check[x][y] = True # 체크 확인 표시
    
    for dx, dy in (-1,0), (1,0), (0,-1), (0,1): # 4방향으로 이동
        nx, ny = x+dx, y+dy
        
        if nx < 0 or nx >= n or ny < 0 or ny >= n: 
            continue # 지역을 넘어가면 pass
        
        if not check[nx][ny] and a[nx][ny] > z:
            dfs(nx, ny, z) # 잠기지 않았고 / 처음 방문한 위치이다 재귀함수 시작


###### 1 ######
n = int(input()) # 안전영역에서 계산해야할 구간은 N * N 이다

a = [list(map(int, input().split())) for _ in range(n)] 
# 입력 받는 데이터: 전체 지역 데이터(이중 list형식)

ans = 0

for k in range(max(map(max, a))): # map(max, a) ==> 각 list(각 행)에서 max값만 추출
                                  # range를 사용한 이유는 구역 최대 값까지의 강수량에 대한 계산만 필요함
                                  # k가 잠기는 지역을 설정함
    
    check = [[False]*n for _ in range(n)] # 확인용 지역 데이터
    
    cnt = 0 # 안전구역 개수 확인용 파라미터
    
    for i in range(n):
        for j in range(n):
            if not check[i][j] and a[i][j] > k:
                
                dfs(i, j, k)
                
                ###### 2_2 ######
                cnt += 1 # 안전구역 조사 끝나면 cnt에 1을 추가하고 다음 안전구역 조사 시작
    
    ans = max(ans, cnt) # k가 변할때 마다 cnt값이 바뀌는데 ans는 cnt가 더 클때마다 업데이트 됨

print(ans) # 최종 결과
