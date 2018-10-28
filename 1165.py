cont=0
tests=int(input())
for i in range(0,tests):
  valor=int(input())
  cont=0
  for j in range(1,valor+1):
    if((valor%j)==0):
        cont+=1
  if(cont==2):
    print(valor,"eh primo")
  else:
    print(valor,"nao eh primo")