def findsausoo(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
#M, N = map(int, input().split())
M = int(input())
N = int(input())
listBefore = []

for i in range(M, N+1):
    if findsausoo(i):
        listBefore.append(i)

if listBefore:
    print(sum(listBefore))
    print(min(listBefore))
else:
    print(-1)