""""
push X: 정수 X를 큐에 넣는 연산이다.
pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 큐에 들어있는 정수의 개수를 출력한다.
empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""
from collections import deque
import queue
import sys
import time


result = int(sys.stdin.readline().strip())
startQueue = deque()

for i in range(result):
    
    getCommand = sys.stdin.readline().strip().split()
    if getCommand[0] == "push":
        startQueue.append(int(getCommand[1]))
    elif getCommand[0] =="pop":
        print(startQueue.popleft() if startQueue else -1)
    elif getCommand[0] =='size':
        print(len(startQueue))
    elif getCommand[0] =='empty':
        print(0 if startQueue else 1)
    elif getCommand[0] =='front':
        print(startQueue[0] if startQueue else -1)
    elif getCommand[0] == 'back':
        print(startQueue[-1] if startQueue else -1)


'''
que 로하면 시간 초과함.
멀티 쓰레드 지원을 위해서 Lock을 사용함
put get 연산이 상대적으로 느림.
'''
#que선언
#startQueue = queue.Queue()
#startQueue.put(int(getCommand[1]))
#print(startQueue.get() if not startQueue.empty() else -1)
#print(startQueue.qsize())  
#print(1 if startQueue.empty() else 0)
#print(startQueue.queue[0] if not startQueue.empty() else -1)
#print(startQueue.queue[-1] if not startQueue.empty() else -1)