test = int(input())
for i in range(0,test):
  cont = 0
  lista = []
  test_1 = int(input()) 
  for i in range(0,test_1):
    lista.append(input())
  for j in range(0,test_1):
    if(lista[j] == 'LEFT'):
      cont=cont-1
    elif(lista[j] == 'RIGHT'):
      cont=cont+1
    else:
      lista[j] = lista[j].split()
      lista[j] = lista[j][len(lista[j])-1]
      lista[j] = lista[int(lista[j])-1]
      if(lista[j]=='LEFT'):
        cont-=1
      else:
        cont+=1
  print(cont)
