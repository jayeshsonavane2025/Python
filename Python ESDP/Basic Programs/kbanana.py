k,n,w=map(int,input().split())
ans=0
for i in range(1,w+1):
    ans += i*k
if ans>=n:
    print(ans-n)
else:
    print(0)