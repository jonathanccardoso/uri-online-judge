while True:
  try:
    go,back=map(int, input().split())
    res=list(map(int, input().split()))
    if(go==back):
      print("*")
    else:
      u=""
      result=[]
      for j in range(0,go):
        result.append(j+1)
      for i in range(0,len(result)):
        count=0
        for k in range(0,len(res)):
          if(result[i]==res[k]):
            count+=1
        if(count==0):
          u+=str(result[i]) + " "
      print(u)
  except EOFError:
    break