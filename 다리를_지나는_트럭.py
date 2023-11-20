#큐를 사용하여 시간을 계산하자
#트럭의 순서가 정해져있음을 잊지말자



def solution(bridge_length, weight, truck_weights):
 
  answer = 0
 	#주어진 길이를 가지는 다리 구현
 	bridge = [0 for _ in range(bridge_length)]
 
 	while bridge:
 
 		answer += 1
		bridge.pop(0) #head 원소 빼기 (Q poping)
 
		if truck_weights:
			if sum(bridge) + truck_weights[0] <= weight: 
				t = truck_weights.pop(0)
				bridge.append(t)
			else: #견딜 수 있는 무게 초과 경우
				bridge.append(0)
 
 
	return answer


