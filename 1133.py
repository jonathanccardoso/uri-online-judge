n=int(input())
m=int(input())
if(n<=m):
  for i in range(n+1,m):
    if((i%5)==2 or (i%5)==3):
      print(i)
else:
  for i in range(m+1,n):
    if((i%5)==2 or (i%5)==3):
      print(i)