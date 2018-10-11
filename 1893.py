a,b=map(int,input().split())
if(a<b):
	if(b>=3 and b<=93):
		result=("crescente")
elif(b<a):
	if(b<=96 and b>=3):
		result=("minguante")
if(b>=0 and b<=2):
	result=("nova")
if(b>=97 and b<=100):
	result=("cheia")
print(result)
