def solution(progresses,speeds):
    answer = []

    while progresses:
        # progress와 해당 progress의 speeds를 계속 더해줌
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        # 완료된 progress
        finishedPro = 0

        # progress가 남아있고, 제일 우선순위 progress 진행도가 100 이상이 된 경우
        while progresses and progresses[0] >= 100:
            # progresses의 제일 첫 번째를 pop
            progresses.pop(0)
            # pogresses의 해당 speeds도(역시 제일 첫 번째) pop
            speeds.pop(0)
            # 완료된 progress 수 카운드
            finishedPro += 1

        # 완료된 progress가 있으면 answer에 추가
        if finishedPro > 0:
            answer.append(finishedPro)

    return answer


result = solution([93,30,55],[1,30,5])
print(result)