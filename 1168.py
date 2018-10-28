l = [6,2,5,5,4,5,6,3,7,6]
n = int(input())
for i in range(n):
  res = 0
  test = input()
  for t in test:
    res += l[int(t)]
  print('%d leds' %int(res))