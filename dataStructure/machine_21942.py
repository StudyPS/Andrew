import sys
from datetime import datetime, timedelta

input = sys.stdin.readline

N, L, F = input().strip().split()
N = int(N)
F = int(F)

d, hm = L.split('/')
h, m = map(int, hm.split(':'))
rental_time = timedelta(days=int(d), hours=h, minutes=m)

borrow = {} #빌린날
fine = {}  #벌금

for i in range(N):
    line = input().strip()
    date_str, time_str, item, user = line.split()
    now = datetime.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M")
    key = item + " " + user
    
    if key not in borrow:
        borrow[key] = now  # 처음 빌림
    else:
        start = borrow.pop(key)  # 대여 시각 꺼내기
        deadline = start + rental_time
        if now > deadline: 
            overdue = now - deadline #넘어간 시간가져오기기
            minutes = overdue.days * 24 * 60 + overdue.seconds // 60
            if user not in fine:
                fine[user] = 0
            fine[user] += minutes * F #추가가

if fine:
    for name in sorted(fine):
        print(name, fine[name])
else:
    print("-1") #//만약 벌금을 내야하는 사람들이 없는 경우는 -1을 출력한다.

    



