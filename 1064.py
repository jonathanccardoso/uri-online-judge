soma = 0
valor = 0
for i in range(0,6):
  valores=float(input())
  if(valores > 0):
    valor+=1
    soma+=valores
media=soma/valor
print(valor, "valores positivos")
print("{:.1f}".format(media))
