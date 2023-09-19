
n=int(input())
a=[]
alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
result=[]
for _ in range(n):
    tmp=input()
    a.append(tmp)
for i in a:
    for j in range(len(i)):
        num=10 ** (len(i)-j-1)
        alphabet_dict[i[j]]+=num
for value in alphabet_dict.values():
    if value >0:
        result.append(value)
result.sort()
answer=0
for i in range(len(result)):
    answer+=result[i]*(9-i)
print(answer)

    
  
