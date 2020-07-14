from pwn import *
from random import seed, randint as w
from time import time

start = int(time())

conn = remote('challenge.rgbsec.xyz', 12345)
conn.recvline()
arr = []
for _ in range(10):
	arr.append(int(conn.recvline()))
offset = len("Here's another number I found: ")
line = conn.recvline()
n = int(line[offset:])
conn.close()

end = int(time())

byt = n.to_bytes((n.bit_length() + 7) // 8, 'little')

for seedval in range(start - 100, end + 100):
	seed(seedval)
	newarr = []
	for _ in range(10):
		newarr.append(w(5, 10000))
	if newarr != arr:
		continue
	b = bytearray([w(0, 255) for _ in range(40)])
	for i in range(len(byt)):
		print(chr(byt[i] ^ b[i]), end="")
	print()
