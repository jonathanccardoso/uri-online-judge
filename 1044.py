n=input()
a,b=n.split(" ")
if(int(b)%int(a)==0 or int(a)%int(b)==0):
  print("Sao Multiplos")
else:
  print("Nao sao Multiplos")
