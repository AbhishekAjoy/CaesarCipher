x = int(input("\n--CAESAR CIPHER--\n1. Encrypt \n2. Decrypt \nEnter choice:"))
res=""
if x == 1:
	p = input("Enter Plain text:")
	for i in p:
		x = ord(i)
		if x >= 65 and x <=90:
			v = (x+3 - 65)%26 + 65
			res = res + chr(v)
		if x >= 97 and x <=122:
			v = (x+3 - 97)%26 + 97
			res = res + chr(v)
	print("Cipher Text:",res)
if x == 2:
	p = input("Enter Cipher text:")
	for i in p:
		x = ord(i)
		if x >= 65 and x <=90:
			v = (x-3 - 65)%26 + 65
			res = res + chr(v)
		if x >= 97 and x <=122:
			v = (x-3 - 97)%26 + 97
			res = res + chr(v)
	print("Plain Text:",res)	
