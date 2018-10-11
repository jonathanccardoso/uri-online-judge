positivo, negativo, par, impar = 0, 0, 0, 0
for i in range(0,5):
  valores=int(input())
  if(valores%2 == 0):
    par+=1
  if(valores%2 != 0):
    impar+=1
  if(valores > 0):
    positivo+=1
  if(valores < 0):
    negativo+=1

print(par,"valor(es) par(es)")
print(impar,"valor(es) impar(es)")
print(positivo, "valor(es) positivo(s)")
print(negativo, "valor(es) negativo(s)")
