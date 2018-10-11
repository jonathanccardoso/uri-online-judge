n=input()
p,r=n.split(" ")
if(int(p)==0):
  print("C")
else:
  if(int(p)==1 and int(r)==0):
    print("B")
  if(int(p)==1 and int(r)==1):
    print("A")
