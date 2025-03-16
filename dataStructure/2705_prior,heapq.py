
'''
메모리, 시간 35508	876
'''
import sys
import heapq

number = int(sys.stdin.readline().strip())
heap = []

for _ in range(number):
    numbers = list(map(int, sys.stdin.readline().split()))
    for i in numbers:
        if len(heap) < number:
            heapq.heappush(heap, i) 
        else:
            if heap[0] < i:
                heapq.heappop(heap)
               
                heapq.heappush(heap, i)
                
print(heap[0])


'''
메모리, 시간간	39764	1760
import sys
from queue import PriorityQueue

N = int(sys.stdin.readline().strip())
prior = PriorityQueue()

for _ in range(N):
    numbers = list(map(int, sys.stdin.readline().split()))
    for num in numbers:
        if prior.qsize() < N: 
            prior.put(num)
        else:  
            if prior.queue[0] < num:
                prior.get() 
                prior.put(num)  
print(prior.get())  



'''
            
