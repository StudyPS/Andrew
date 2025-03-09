

'''
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''


import sys
from collections import deque

deck = deque()
rangeNumber = int(sys.stdin.readline().strip())

for i in range(rangeNumber):
    command = sys.stdin.readline().split()

    if command[0] == 'push_front':
        deck.appendleft(command[1])
    elif command[0] == 'push_back':
        deck.append(command[1])
    elif command[0] =='pop_front':
        if deck:
            print(deck[0])
            deck.popleft()
        else:
            print("-1")
    elif command[0] == 'pop_back':
        if deck:
            print(deck[-1])
            deck.pop()
        else:
            print("-1")
    elif command[0] == "size":
        print(len(deck))
    elif command[0] == 'empty':
        if deck:
            print("0")
        else:
            print("1")
    elif command[0] == 'front':
        if deck:
            print(deck[0])
        else:
            print("-1")
    elif command[0] =='back':
        if deck:
            print(deck[-1])
        else:
            print("-1")


        
    