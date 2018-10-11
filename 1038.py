n=input()
a,b=n.split(" ")
v2=0.00
if(int(a)==1):
  v2=4.00
else:
  if(int(a)==2):
    v2=4.50
  if(int(a)==3):
    v2=5.00
  if(int(a)==4):
    v2=2.00
  if(int(a)==5):
    v2=1.50
print("Total: R$ {0:.2f}".format(v2*int(b)))
