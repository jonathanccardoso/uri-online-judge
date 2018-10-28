while True:
  h1, m1, h2 , m2 = map(int, input().split())
  x=0
  y=0
  if h1 == m1 == h2 == m2 == 0:
    break
  else:
    x = h1*60 + m1
    y = h2*60 + m2
    if(y <= x):
      y += 24*60  
    print(abs(y-x))