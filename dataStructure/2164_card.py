'''
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.

이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 버린 카드들은 순서대로 1 3 2가 되고, 남는 카드는 4가 된다.

N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램을 작성하시오.

'''

import sys
from collections import deque

getInput = int(sys.stdin.readline().strip())

card = deque()
#card = deque(range(1, getInput +1)  - for 문 돌린거랑 안돌린거 - 164 ms   돌린거 192ms
for i in range(1, getInput + 1):
    card.append(i)

while len(card) > 1:
    card.popleft()
    card.append(card.popleft())

print(card[0])
'''
card = []
for i in range(1, getInput + 1):
    card.append(i)
    
while len(card) > 1:
    card.pop(0)
    card.append(card.pop())

print(card)
'''
