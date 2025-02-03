import sys
res={}
for line in sys.stdin:
	key,value=line.strip().split('\t')
	res[key]=value
op=""
c=0
for el in res.values():
	op=op+str(el)
	op+='\t'
	c+=1
	if c%3==0:
		op+="\n"
print(op)
