import sys
a=[[10,20,30],[40,50,60],[70,80,90]]
for i in range(3):
	for j in range(3):
		key=f"{i},{j}"
		res=a[j][i]
		print(f"{key}\t{res}")
		
