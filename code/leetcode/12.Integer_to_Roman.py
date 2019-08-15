def intToRoman(num):
	"""
	:type num: int
	:rtype: str
	"""
	roman_data = ""
	int_Data = str(num)
	num_len = len(int_Data)
	for i in range(num_len-1,-1,-1):
		data = int(int_Data[num_len-1-i])
		if i == 3:
			roman_data = data * "M"
		elif i == 2:
			if data == 9:
				roman_data += "CM"
			elif 5 <= data:
				roman_data += "D" + (data-5) * "C"
			elif data == 4:
				roman_data += "CD"
			else:
				roman_data += data * "C"
		elif i == 1:
			if data == 9:
				roman_data += "XC"
			elif 5 <= data:
				roman_data += "L" + (data-5) * "X"
			elif data == 4:
				roman_data += "XL"
			else:
				roman_data += data * "X"
		else:
			if data == 9:
				roman_data += "IX"
			elif 5 <= data:
				roman_data += "V" + (data-5) * "I"
			elif data == 4:
				roman_data += "IV"
			else:
				roman_data += data * "I"
	return roman_data

print(intToRoman(14))