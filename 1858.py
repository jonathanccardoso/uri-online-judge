x=int(input())
xx=[int(y) for y in input().split(" ")]
n,t=xx[0],0
for i in range(x):
  if(xx[i] < n):
    n,t=xx[i],i
print(t+1)