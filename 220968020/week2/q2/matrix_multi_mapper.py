import sys
a=[[10,20,30],[40,50,60],[70,80,90]]
b=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
	for j in range(3):
		key=f"{i},{j}"
		res = sum(a[i][k] * b[k][j] for k in range(3))
		print(f"{key}\t{res}")
		
