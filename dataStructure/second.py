'''

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
'''

import sys 

#list 선언
list = []
result = int(sys.stdin.readline().strip())

for i in range(result):
    getCommand = sys.stdin.readline().strip().split()
    if(getCommand[0] == 'push'):
        list.append(int(getCommand[1]))
    elif (getCommand[0] == 'pop'):
        print(list.pop() if list else -1)
    elif (getCommand[0] == 'size'):
        print(len(list))
    elif (getCommand[0]) == 'empty':
        print(1 if len(list) == 0 else 0)
    elif (getCommand[0]) == 'top':
        print(list[-1] if len(list) >0 else -1)


        
        


