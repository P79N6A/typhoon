# 一个随机产生（1，2，3），变为随机产生（1，2，3，4，5）


def fdf(data):
	num=0
	while data:
		data = data//5
		num+=data
	return num
print(fdf(125))
