def solution(people, limit):
    people.sort()
    heavyIndex = len(people)-1
    rightIndex = 0
    weightNow = 0
    answer = 1
    peopleCountInBoat = 0
    
    while rightIndex != heavyIndex:

        if peopleCountInBoat == 0:
            weightNow += people[heavyIndex]
            heavyIndex -= 1
            peopleCountInBoat += 1
        else:
            if (weightNow + people[rightIndex]) <= limit:
                rightIndex += 1
                peopleCountInBoat = 0
                weightNow = 0
                answer += 1

            else :
                peopleCountInBoat = 0
                weightNow = 0
                answer += 1


    if weightNow + people[rightIndex] > limit:
        answer += 1
    return answer