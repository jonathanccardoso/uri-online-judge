cards = list(map(int, input().split()))
ct = len(cards)

for i in range(1, ct):
  if cards[i-1] < cards[i]:
    ct -= 1
  else:
    if cards[i-1]>cards[i]:
      ct += 1

if ct == 1:
  print('C')
else:
  if ct==2*len(cards)-1:
    print('D')
  else:
    print('N')