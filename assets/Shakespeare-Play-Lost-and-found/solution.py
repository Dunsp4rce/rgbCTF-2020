text = open("play").read().split('\n')

indices = open("some_numbers.txt").read().split('\n')

flag = ""
for line in indices:
	x, y = line.split(',')
	x, y = int(x), int(y)
	flag += text[x][y]

flag = "rgbCTF{" + flag + "}"
print(flag)