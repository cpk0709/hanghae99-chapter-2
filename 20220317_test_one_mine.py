from collections import deque
# [ ,30,55],[1,30,5]
def solution(progresses,speeds):
    answer = []
    progresses_ch = deque(progresses)
    speeds_ch = deque(speeds)

    while progresses_ch:
        # progress와 해당 progress의 speeds를 계속 더해줌
        for i in range(len(progresses_ch)):
            progresses_ch[i] += speeds_ch[i]

            # print(progresses_ch[i])

        # 완료된 progress
        finishedPro = 0

        # progress가 남아있고, 제일 우선순위 progress 진행도가 100 이상이 된 경우
        while progresses_ch and progresses_ch[0] >= 100:
            # progresses의 제일 첫 번째를 pop
            progresses_ch.popleft()
            # pogresses의 해당 speeds도(역시 제일 첫 번째) pop
            speeds_ch.popleft()
            # 완료된 progress 수 카운드
            finishedPro += 1

        # print(finishedPro)

        # 완료된 progress가 있으면 answer에 추가
        if finishedPro > 0:
            answer.append(finishedPro)

    # print(answer)
    return answer


result = solution([93,30,55],[1,30,5])
print(result)