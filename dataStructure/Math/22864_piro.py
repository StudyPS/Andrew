A,B,C,M = map(int, input().split())

piro = 0
workhour = 0
hour = 24

while hour !=0:
    if A > M:
        break #피로도 넘으먹 브레이크
    elif piro + A > M:
        piro -=C #쉬기
        hour -=1
        if piro < 0:
            piro = 0
    else:
        piro += A
        workhour += B
        hour -= 1
print(workhour)