import sys

N, K = map(int, sys.stdin.readline().split())

nList = list(range(1, N+1)) # 리스트 입력받은곳 (n개)
popResult = [] ## 제거해서 넣을곳
pointer = 0
while len(nList) > 0:
    pointer = (pointer + K -1) % len(nList)
    popResult.append(nList.pop(pointer))


print("<" + ", ".join(map(str, popResult)) + ">")
