while True:
  try:
    n=int(input())
    list_n=list(reversed(str(n)))
    size_n=len(list_n)
    for i in range(0,size_n):
      if(i==(size_n-1)):
        print(list_n[i], end="\n")
      else:
        print(list_n[i], end="")
    break
  except:
    break