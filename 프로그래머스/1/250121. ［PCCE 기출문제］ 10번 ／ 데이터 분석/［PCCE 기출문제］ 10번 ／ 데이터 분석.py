def solution(data, ext, val_ext, sort_by):
    diction = {"code":0, "date":1, "maximum":2, "remain":3}
    answer = []
    for i in range(len(data)):
        if data[i][diction[ext]] < val_ext:
            answer.append(data[i])
    answer.sort(key= lambda x:x[diction[sort_by]])
    return answer