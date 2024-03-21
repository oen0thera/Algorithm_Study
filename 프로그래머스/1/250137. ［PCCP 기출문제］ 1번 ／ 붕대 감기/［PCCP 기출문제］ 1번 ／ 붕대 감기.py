def solution(bandage, health, attacks):
    max_time = 0
    for i in attacks:
        if i[0]>=max_time:
            max_time = i[0]
    attack_seq = 0
    next_attack = attacks[attack_seq]
    curr_health = health
    heal_seq = 0
    for time in range(max_time+1):
        if time == next_attack[0]:
            curr_health-=next_attack[1]
            heal_seq=0
            if curr_health<=0:
                return -1
            if attack_seq<len(attacks)-1:
                attack_seq+=1
                next_attack=attacks[attack_seq]
            continue
        else:
            if curr_health==health:
                continue
            else:
                curr_health+=bandage[1]
                if curr_health>=health:
                    curr_health=health
                heal_seq+=1
                if heal_seq==bandage[0]:
                    heal_seq=0
                    curr_health+=bandage[2]
                    if curr_health>=health:
                        curr_health = health
    answer = curr_health
    return answer