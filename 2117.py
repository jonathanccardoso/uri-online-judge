termino_minutos=int(input())
n=input()
presente_1,presente_2=n.split(" ")
tempo_presente=int(presente_1)+int(presente_2)
if(termino_minutos < tempo_presente):
  print("Deixa para amanha!")
else:
  print("Farei hoje!")
