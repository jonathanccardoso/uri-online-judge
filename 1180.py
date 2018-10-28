x=int(input())
xx=list(map(int,input().split()))
m,p=[xx[0],1]

for i in range(1,x):
  if(xx[i] < m):
    m=xx[i]
    p=i
print("Menor valor:", str(m))
print("Posicao:", str(p))