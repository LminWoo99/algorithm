n, m=map(int, input().split())
a=list(map(int, input().split()))
a=sorted(a, reverse=True)
print(a[m-1])