import sys
from collections import defaultdict

def length(dic):
	min_l = 10000
	max_l = 0
	for i in dic:
		for j in range(len(dic[i])-k + 1):
			length = dic[i][j+k-1] - dic[i][j] + 1
			min_l = min(min_l,length)
			max_l = max(max_l,length)
	return(min_l,max_l)
			
t = int(sys.stdin.readline())
for _ in range(t):
	word = sys.stdin.readline().strip()
	k = int(input())
	dic = defaultdict(list)
	for i in range(len(word)):
		if word.count(word[i]) >= k:
			dic[word[i]].append(i)
	if not dic:
		print(-1)
	else:
		print(*length(dic))