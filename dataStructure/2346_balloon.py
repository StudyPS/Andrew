'''
1번부터 N번까지 N개의 풍선이 원형으로 놓여 있고. list =[N-1]
 i번 풍선의 오른쪽에는 i+1번 풍선이 있고,   이 i번이 뭐임?? 어디서가져옴????  
 왼쪽에는 i-1번 풍선이 있다. 
 단, 1번 풍선의 왼쪽에 N번 풍선이 있고,  -> 동그라미로 있으니까    ㅇㅋ 
   N번 풍선의 오른쪽에 1번 풍선이 있다.  idx
   
   각 풍선 안에는 종이가 하나 들어있고, 
   종이에는 -N보다 크거나 같고, N보다 작거나 같은 정수가 하나 적혀있다.  -N<=종이 <=N
     이 풍선들을 다음과 같은 규칙으로 터뜨린다.

우선, 제일 처음에는 1번 풍선을 터뜨린다.  list[0]
다음에는 풍선 안에 있는 종이를 꺼내어 그 종이에 적혀있는 값만큼 이동하여 다음 풍선을 터뜨린다.
양수가 적혀 있을 경우에는 오른쪽으로, 음수가 적혀 있을 때는 왼쪽으로 이동한다.  if(풍선 < 0) 오른쪽 if(풍선>0) 왼쪽
이동할 때에는 이미 터진 풍선은 빼고 이동한다. list.pop

예를 들어 다섯 개의 풍선 안에 차례로 3, 2, 1, -3, -1이 적혀 있었다고 하자. 
이 경우 3이 적혀 있는 1번 풍선,
 -3이 적혀 있는 4번 풍선, 
 -1이 적혀 있는 5번 풍선, 
 1이 적혀 있는 3번 풍선,
2가 적혀 있는 2번 풍선의 순서대로 터지게 된다.
'''

# 메모리 34908 시간 52
import sys
from collections import deque 

getInput = int(sys.stdin.readline().strip())
getData = sys.stdin.readline().strip().split()
dek = deque(enumerate(map(int, getData)))

result = []
popindex, value = dek.popleft()
result.append(popindex + 1)


while dek:
  if value > 0:
    dek.rotate(-(value-1))
  else:
    dek.rotate(-value)

  popindex, value = dek.popleft()
  result.append(popindex + 1)

print(*result)


# 메모리 34924 시간 144
# import sys
# from collections import deque 

# getInput = int(sys.stdin.readline().strip())

# getData = sys.stdin.readline().strip().split()
# dek = deque(enumerate(map(int, getData)))

# result = []
# deklist = [[index, value] for index, value in dek]

# popindex, value = deklist.pop(0)
# result.append(popindex + 1)

# while deklist:
#     if value > 0:
#         for i in range(value - 1):
#             deklist.append(deklist.pop(0))
#     else:
#         for i in range(-value):
#             deklist.insert(0, deklist.pop())

#     popindex, value = deklist.pop(0)
#     result.append(popindex + 1)

# print(*result)
