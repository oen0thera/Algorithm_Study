def solution(bandage, health, attacks):
    answer = 0
    success = 0
    attacks_index = 0
    sec_count = 0
    max_health = health
    
    for i in range(1, attacks[-1][0]+1):
        # 공격 먼저 
        if attacks[attacks_index][0] == i:
            health -= attacks[attacks_index][1]
            attacks_index += 1
            sec_count = 0
        else: 
            health += bandage[1]
            sec_count += 1
            if sec_count == bandage[0]:
                health += bandage[2]
                sec_count = 0
            
        if health <= 0: 
            return -1
        if health >= max_health:
            health = max_health

    return health