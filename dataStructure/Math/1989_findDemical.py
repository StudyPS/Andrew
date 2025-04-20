N = int(input())
data = list(map(int, input().split()))
count = 0

def findsausoo(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in data:
    if findsausoo(i):
        count += 1

print(count) 