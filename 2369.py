n=int(input())
preco=0
if(n<=10):
  preco=7
else:
  if(n>=11 and n<=30):
    preco=7+(n-10) * 1
  if(n>=31 and n<=100):
    preco=27+(n-30) * 2
  if(n>=101):
    preco=167+(n-100) * 5
print(preco)
