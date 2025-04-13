from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(sys.stdin.readline().strip()) #5


difficult = []
easy =[]
nando = {} # 번호, 난이도
doneProblem = [] 


for _ in range(n):
    p, l = map(int, input().split())
    heappush(difficult, (-l, -p))
    heappush(easy, (l, p))
    nando[p] = l

commandCount = int(sys.stdin.readline().strip()) #명령어수
for _ in range(commandCount):
    command = list(sys.stdin.readline().strip().split())

    if command[0] == 'recommend':
        if command[1] == '1':
            while True:
                l, p = difficult[0]  
                if (-l, -p) in doneProblem:
                    heappop(difficult)
                else:
                    print(-p)
                    break
        else:
            while True:
                l, p = easy[0]
                if (l, p) in doneProblem:
                    heappop(easy)
                else:
                    print(p)
                    break

    elif command[0] == 'add':
        p, l = int(command[1]), int(command[2])
        heappush(difficult, (-l, -p))
        heappush(easy, (l, p))
        nando[p] = l
        if (l, p) in doneProblem:
            doneProblem.remove((l, p))

    elif command[0] == 'solved':
        p = int(command[1])
        l = nando[p]
        doneProblem.append((l, p))

