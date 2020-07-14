enc = open("punchline.txt").read()

flag = ""
for i in enc:
	if i in ["{", "}", "_"]:
		flag += i
		continue
	b = False
	val = ord(i)
	if ord(i) < ord('a'):
		b = True
		val -= ord('A')
	else:
		val -= ord('a')
	val -= 11
	val %= 26
	if b:
		val += ord('A')
	else:
		val += ord('a')
	flag += chr(val)

print(flag)