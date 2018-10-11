a,b=map(int,input().split())
if(a>b):
  print("O JOGO DUROU", (24-a)+b, "HORA(S)")
elif(a==b):
  print("O JOGO DUROU", 24, "HORA(S)")
elif(a<b):
  print("O JOGO DUROU", b-a, "HORA(S)")
