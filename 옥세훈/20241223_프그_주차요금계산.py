import math

def solution(fees, records):
    answer = []
    dic = dict()
    car = dict()
    
    for i in records:
        time, car_num, state = i.split(" ")
        time = time.split(":")
        time1 = int(time[0]) * 60 + int(time[1])
        
        # 입장
        if state == "IN":
            dic[car_num] = [time1, state]
        if car_num not in car:
            car[car_num] = [0, state]
        elif car_num in car and state == "IN":
            car[car_num][1] = "IN"
        else:
            # 찍혀있고, 출차를 한다면
            if state == "OUT":
                calcul_time = (time1 - dic[car_num][0])
                car[car_num][0] += calcul_time
                car[car_num][1] = "OUT"
                
                
    for i in car.keys():
        if car[i][1] == "IN":
            temp = 1439 - dic[i][0]
            car[i][0] += temp
                
                
    for i in car.keys():
        if car[i][0] > fees[0]:
            cost = fees[1] + math.ceil((car[i][0]-fees[0]) / fees[2]) * fees[3]
            car[i][0] = cost
        else:
            car[i][0] = fees[1]
            
    
    check = sorted(car.keys(), key=lambda x : x)
    
    for i in check:
        answer.append(car[i][0])
        
    return answer