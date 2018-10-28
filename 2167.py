t=int(input())
y=input().split()
k=[]
xu=0

for ix, i in enumerate(y):
  if int(i) >= int(xu):
    xu=i
  else:
    k.append(ix+1)
if(k==[]):
  print("0")
else:
  print(k[0])