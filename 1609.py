t=int(input())
while(t!=0):
  k=int(input())
  y=list(map(int, input().split()))
  y.sort()
  cont=0
  for i in range(0, (len(y))):
    if(y[i]==y[i-1]):
      cont+=1
  if(len(y)-cont==0):
    print(1)
  else:
    print(len(y)-cont)
  t-=1