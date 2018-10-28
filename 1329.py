while True:
  n=int(input())
  if(n==0):
    break
  else:
    lista=list(map(int,input().split()))
    print("Mary won {} times and John won {} times".format(lista.count(0), lista.count(1)))