qt = int(input())
l = {}
for i in range(qt):
  n = int(input())
  if n in l:
    l[n] += 1
  else:
    l[n] = 1

fq = l.keys()
fq = sorted(fq)

for j in fq:
  print("%d aparece %d vez(es)" %(j,l[j]))
