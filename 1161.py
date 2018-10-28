def fatorial(x):
  fat_n=1
  for i in range(1,x+1):
    fat_n= fat_n*i
  return fat_n

while True:
  try:
    n_a,n_b = map(int,input().split())
    fatorial_a = fatorial(n_a)
    fatorial_b = fatorial(n_b)    
    soma_fat = fatorial_a + fatorial_b
    print(soma_fat)
  except:
    break