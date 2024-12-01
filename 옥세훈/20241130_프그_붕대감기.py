def solution(bandage, health, attacks):
    max_h = health
    
    time = 0
    for i in range(len(attacks)):
        attack_time, damage = attacks[i]
        
        check = attack_time - time - 1
        
        cnt = 0
        for i in range(check):
            if health + bandage[1] < max_h:
                # print(health, "health")
                health += bandage[1]
            else:
                health = max_h
            cnt += 1
            
            if cnt == bandage[0]:
                if health + bandage[2] < max_h:
                    health += bandage[2]
                else:
                    health = max_h 
                cnt = 0
                
        
        if health - damage <= 0:
            return -1
        else:
            health -= damage
            print(health)
            
        time = check  
    
    return health