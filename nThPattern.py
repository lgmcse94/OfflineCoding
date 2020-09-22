n=int(input("n="))
data=[]
for i in range(1,n+1):
	s=""
	for j in range(1,i+1):
		s=s+" "+str(i)
	for k in range(j+1,n+1):
		s=s+" "+str(k)
	sr=s.strip().split(" ")
	del sr[0]
	for val in sr:
		s=str(val)+" "+s.strip()
	data.append(s)
data.reverse()
for v in data:
	print(v)
data.reverse()
del data[0]
for v in data:
	print(v)