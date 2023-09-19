n=int(input())
i=2
while True:
   if n==1:
       break
   else:
        if n%i==0:
            print(i)
            n/=i
        else:
            i+=1