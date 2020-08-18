# 다리를 지나는 트럭 
def solution(bridge_length, weight, truck_weights):
    answer = 0 # 시간
    crossing = [0] * bridge_length # 다리
    
    while crossing: # 다리위 아무것도 없을때 까지 반복
        
        answer += 1 # 시간 증가
        crossing.pop(0) # 다리 당기기
        
        if truck_weights: # 대기중인 트럭이 있을때
            
            if sum(crossing) + truck_weights[0] <= weight: # 다리가 수용 가능하다면
                crossing.append(truck_weights.pop(0)) # 대기중이던 트럭 출발
            
            else: # 다리가 수용 불가능 할때는
                crossing.append(0) # 빈공간 추가
    return answer
crossing = [0] * 5
while crossing:
    print(1)
    crossing.pop()

solution(2, 10, [7, 4, 5, 6])

# 오답 나옴...!!
# 왜? : ??????

def solution(bridge_length, weight, truck_weights):
    answer = 0 # 시간
    bridge_on = [0]* bridge_length # 다리 위 
    curr_weight = 0
    
    
    # 출발지에 트럭이 있을 경우 실행되는 라인
    while truck_weights: # 대기중인 차가 있으면 계속 반복 없으면 중단
        answer+=1 # 시간 증가
        bridge_out = bridge_on.pop(0) # 1초 증가할때 한칸씩 당겨짐
        curr_weight -= bridge_out # 다리위 무게 -bridge_out은 빈칸이 당겨질때는 상관이 없고
                                  # 차량이 나가면 그만큼 다리위 무게가 줄어듦

        if curr_weight + truck_weights[0] > weight: # 다리가 수용불가능하면
            bridge_on.append(0)                     # 차는 못들어오고 빈칸이 들어옴
            
        else: # 다리가 수용가능하다면
            truck = truck_weights.pop(0) # 기다리던 트럭이 들어오고
            bridge_on.append(truck)
            curr_weight += truck # 들어온 트럭의 무게 추가

    
    # 모두 트럭을 건너고 마지막 트럭이 다리를 다 건너는 시간을 추가하기 위함 반복문
    while curr_weight>0:
        answer +=1
        bridge_out = bridge_on.pop(0)
        curr_weight -=bridge_out

    return answer