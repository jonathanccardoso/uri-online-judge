ca,ba,pa=map(int, input().split())
cr,br,pr=map(int, input().split())
result=0
if(cr>ca):
  result+=(cr-ca)
if(br>ba):
  result+=(br-ba)
if(pr>pa):
  result+=(pr-pa)
elif(cr==ca or br==ba or pr==pa):
  result+=0
print(result)
