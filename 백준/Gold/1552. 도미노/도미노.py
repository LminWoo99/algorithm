from  itertools import permutations
def convert_domino(a):
    for i in range(n):
        for j in range(n):
            if a[i][j].isdigit():
                a[i][j]=int(a[i][j])
            else:
                a[i][j]=ord('A')-ord(a[i][j])-1
    return a                
def calculate_score(cycles):
    score = 1
    for cycle in cycles:
        cycle_score = 1
        for (i, j) in cycle:
            cycle_score *= a[i][j]
        score *= cycle_score
    if len(cycles) % 2 == 0:
        score *= -1
    return score        
                
    
    
n=int(input())
a=[list(input().rstrip()) for _ in range(n)]
max_ans=-1
min_ans=int(1e9)

a=convert_domino(a)
domino=list(range(n))
grid=[]
for temp in permutations(domino,n):
    cycles=[]
    visit=[0]*n
    for i in range(n):
        if not visit[i]:
            cycle=[]
            x=i
            while not visit[x]:
                visit[x]=1
                cycle.append((x, temp[x]))
                x=temp[x]
            cycles.append(cycle)
    score=calculate_score(cycles)
    max_ans=max(score, max_ans)
    min_ans=min(score, min_ans)
print(min_ans)
print(max_ans)