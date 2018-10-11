n1,n2,n3,n4=map(float,input().split(" "))
R=((n1*2)+(n2*3)+(n3*4)+(n4*1))/10

print("Media: {:.1f}".format(R))

if(R>7.0):
  print("Aluno aprovado.")

if(R<5.0):
  print("Aluno reprovado.")

if(5.0<=R<=6.9):
  print("Aluno em exame.")

  ne=float(input())

  print("Nota do exame:",ne)

  Rf=(ne+R)/2

  if(Rf>=5.0):
   print("Aluno aprovado.")

  elif(Rf<=4.9):
   print("Aluno reprovado.")

  print("Media final:",Rf)
