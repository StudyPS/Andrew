'''
N = int(input())
numbers = list(map(int, input().split()))

if N == 2:
    M, P = numbers
    for i in range(1, min(M,P)+1):
        if ( M % i ) == 0 and P % i ==0:
            print(i)
elif N == 3:
    M, P, C = numbers
    for j in range(1, min(M, P, C)+1):
        if M % j ==0 and P % j ==0 and C % j ==0:
            print(j)

'''

n = int(input())
numbers = list(map(int, input().split()))

def findGcd(a, b):
    if a < b:
        a, b = b, a
    
    while a !=0:
        b %= a
        a, b = b,a
    return b

gcd = numbers[0]
for i in numbers:
    gcd = findGcd(gcd, i)

divisor = set()
for i in range(1, int(gcd**0.5) +1):
    if gcd % i == 0:
        divisor.add(i)
        divisor.add(gcd // i)

for i in sorted(divisor):
    print(i)