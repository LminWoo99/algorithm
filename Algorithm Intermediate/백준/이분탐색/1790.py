n , k = map(int, input().split())
ans = 0
digit = 1
nine = 9


while k > digit*nine:
    k = k-(digit * nine)
    ans = ans + nine
    digit+=1
    nine = nine*10

ans = (ans+1) + (k-1) // digit
if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1)%digit])
   
    
