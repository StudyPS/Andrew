import sys

treecount = 0
dict_tree = {} #dict_treeionary

while True:
    treeName= sys.stdin.readline().strip()
    if not treeName:
        break

    if treeName in dict_tree:  #있으면 dic에 카운트추가
        dict_tree[treeName] += 1
    else: #없으면 dict_tree에 네임 추가 하고 카운트는 1
        dict_tree[treeName] = 1

    treecount +=1

#다 추가되고
trees = list(dict_tree.keys()) #이름추출
trees.sort() # 순서정렬원하니까까

for i in trees:
    #print(i, round(dict_tree[i] / treecount * 100, 4)) 이거 왜안댐 나중에 찾아봄봄
    print(i, "{:.4f}".format(dict_tree[i] / treecount * 100))
    

