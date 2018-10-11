diametro=int(input())
n=input()
altura,largura,profundidade=n.split(" ")
if(int(diametro) <= int(altura) and int(diametro) <= int(largura) and int(diametro) <= int(profundidade)):
  print("S")
else:
  print("N")
