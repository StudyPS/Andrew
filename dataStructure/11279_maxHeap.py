'''
널리 잘 알려진 자료구조 중 최대 힙이 있다. 최대 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

1.배열에 자연수 x를 넣는다. number = int(sys.stdin.readline())
2/ 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.
'''

import sys
import heapq

number = int(sys.stdin.readline())
maxHeap = []

for _ in range(number):
    inputNumber = int(sys.stdin.readline())

    if inputNumber:
        heapq.heappush(maxHeap, (-inputNumber, inputNumber))

    else:
        if not maxHeap:
            print(0)
        else:
            print(heapq.heappop(maxHeap)[1])
