'''
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다. 스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 
하나의 수열을 만들 수 있다. 
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
이를 계산하는 프로그램을 작성하라.

4 입력 받으면 1,2,3,4 넣고 4빼기 
3입력 받으면 123 에서 3빼기
6입력 받으면 1,2,5,6 6빼기
8입력 받으면
1,2,5,7,8 에서 8 빼기
7입력 7빼기
5입력 5빼기
2입력 2빼기
1입력 1빼기

'''
import sys 


testcount = int(sys.stdin.readline().strip())

stack = []
result = []
num1 = 1
for i in range(testcount):
    num = int(sys.stdin.readline().strip())
    while num1 <= num:
        stack.append(num1)
        result.append('+')
        num1 += 1
    
    if stack[-1] == num:
        result.append('-')
        stack.pop()
    else:
        print("NO")
        sys.exit(0)
for i in result:
    print(i)