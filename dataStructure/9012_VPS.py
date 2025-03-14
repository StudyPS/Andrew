'''
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
   한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
   그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
   예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 
   그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 
'''

''' PS = () 임.'''
#VPS는 올바른 괄호 문자열
# x를 파라미터로해서 (x)도 VPS
#x와 y를 접합문자 xy (xy)도 VPS
#(())()  와 ((()))은 vps
# 그냥 마지막 이랑 첫번째가 (, ) 인지 확인 하면 되는거아님?
import sys



intT = int(sys.stdin.readline().strip()) #정수 T값

for i in range(intT):
    PS = sys.stdin.readline().strip()
    getList = []
    #splitPS = PS.split()
    for j in PS: 
        if j == '(':
            getList.append(j)
        elif j ==')':
            if getList :
                getList.pop()

            else: 
                print("NO")
                break
        
    else: 
        if not getList:
            print("YES")
        else:
            print("NO")

 


