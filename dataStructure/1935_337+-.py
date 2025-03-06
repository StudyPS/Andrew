'''
첫째 줄에 피연산자의 개수(1 ≤ N ≤ 26) 가 주어진다. 
그리고 둘째 줄에는 후위 표기식이 주어진다. 
(여기서 피연산자는 A~Z의 영대문자이며, A부터 순서대로 N개의 영대문자만이 사용되며, 길이는 100을 넘지 않는다) 
그리고 셋째 줄부터 N+2번째 줄까지는 각 피연산자에 대응하는 값이 주어진다.
3번째 줄에는 A에 해당하는 값, 4번째 줄에는 B에 해당하는값 , 5번째 줄에는 C ...이 주어진다, 그리고 피연산자에 대응 하는 값은 100보다 작거나 같은 자연수이다.

후위 표기식을 앞에서부터 계산했을 때, 식의 결과와 중간 결과가 -20억보다 크거나 같고, 20억보다 작거나 같은 입력만 주어진다.

후위 표기식 계산법

123++
2+3 ---> 15+
1+5
=6  숫자나오면 넘어가고 연산자 나오면 해당값앞 2개 + 연산자 해서 나오고 반복
'''

import sys

getInput = int(sys.stdin.readline().strip())
if not 1 <= getInput <= 26:
    sys.exit(1)
asci = sys.stdin.readline().strip()

appendlist =[0] * getInput
for i in range(getInput):
    appendlist[i] = int(sys.stdin.readline().strip())

stack = []
for i in asci:
    if 'A' <= i <='Z': #피연산자 뽑고
        stack.append(appendlist[ord(i) - ord('A')])
    else: #연산자 뽑고
        Ascii2 = stack.pop() 
        Ascii1 = stack.pop() 
    if i == '+':
        stack.append(Ascii1 + Ascii2)
    elif i =='-':
        stack.append(Ascii1 - Ascii2)
    elif i == '*':
        stack.append(Ascii1 * Ascii2)
    elif i == '/':
        stack.append(Ascii1 / Ascii2)

print('%.2f' %stack[0])

