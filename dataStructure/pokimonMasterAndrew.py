'''
첫째 줄에는 도감에 수록되어 있는 포켓몬의 개수 N이랑 내가 맞춰야 하는 문제의 개수 M이 주어져.  => m,m   n= 포켓몬수 m은 남은수?
N과 M은 1보다 크거나 같고, 100,000보다 작거나 같은 자연수인데,  int n, m = <=1000
자연수가 뭔지는 알지? 모르면 물어봐도 괜찮아. 
나는 언제든지 질문에 답해줄 준비가 되어있어.

둘째 줄부터 N개의 줄에 포켓몬의 번호가 1번인 포켓몬부터 N번에 해당하는 포켓몬까지 한 줄에 하나씩 입력으로 들어와. -> 26개가 들어감
포켓몬의 이름은 모두 영어로만 이루어져있고, 또, 음... 첫 글자만 대문자이고, 나머지 문자는 소문자로만 이루어져 있어.  Pikachu
아참! 일부 포켓몬은 마지막 문자만 대문자일 수도 있어. 포켓몬 이름의 최대 길이는 20, 최소 길이는 2야.    -> 일부 포켓몬 마지막 대문자   2<= 포켓몬이름 <=20
그 다음 줄부터 총 M개의 줄에 내가 맞춰야하는 문제가 입력으로 들어와.

 문제가 알파벳으로만 들어오면 포켓몬 번호를 말해야 하고,   알파벳 -> 포켓몬 번호 말하기 
 숫자로만 들어오면, 포켓몬 번호에 해당하는 문자를 출력해야해.  숫자 -> 문자
 입력으로 들어오는 숫자는 반드시 1보다 크거나 같고,   M > 1 && M<=N
 N보다 작거나 같고, 입력으로 들어오는 문자는 반드시 도감에 있는 포켓몬의 이름만 주어져. 그럼 화이팅!!!
'''

import sys

numberForPokeMon = sys.stdin.readline().strip().split()
N, M = map(int, numberForPokeMon)

PokemonDogamName = {}
PokemonDoganNumber = {}
for i in range(1, 1 + N):
    value = sys.stdin.readline().strip()
    PokemonDogamName[i] = value
    PokemonDoganNumber[value] = i

for _ in range(M):
    Poke = sys.stdin.readline().strip()
    if Poke.isdigit():
        print(PokemonDogamName[int(Poke)])
    else:
        print(PokemonDoganNumber[Poke])








'''
example input
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna
'''

