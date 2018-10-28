t,s = map(int,input().split())
y = True
k = list(map(int,input().split()))

for i in range(0,len(k)-1):
  if abs(k[i]-k[i+1]) > t:
    y = False
if y == True:
  print("YOU WIN")
else:
  print("GAME OVER")