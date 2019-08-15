def fdf(data):
	num=0
	while data:
		data = data//5
		num+=data
	return num
print(fdf(125))
