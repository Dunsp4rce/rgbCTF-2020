import base64

f = open("basic_chall.txt").read().split()

hs = ""
for b in f:
	hs += chr(int(b, 2))

b64 = ""
for h in hs.split():
	b64 += chr(int(h, 16))

oc = base64.b64decode(b64).decode().split()

sol = ""
for i in oc:
	sol += chr(int(i, 8))

print(sol)