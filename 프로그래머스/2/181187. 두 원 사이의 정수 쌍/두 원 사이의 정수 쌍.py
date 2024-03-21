def solution(r1, r2):
    # x, y축 위에 있는 점 구하기
    dotOnLineCount = r2 - r1 + 1
    answer = 0
    for i in range(0, r2+1):
        if i == 0:
            answer += r2-r1+1
        elif 0 < i < r1 :
            y1 = ((r1 ** 2 - i ** 2) ** (1/2)) 
            if y1%1 == 0:
                y1 = y1 // 1
            else: 
                y1 = y1 // 1 + 1
            y2 = ((r2 ** 2 - i ** 2) ** (1/2)) // 1

            answer += y2-y1+1
        else: 
            y2 = ((r2 ** 2 - i ** 2) ** (1/2)) // 1
            answer += y2+1

    return answer * 4 - dotOnLineCount*4