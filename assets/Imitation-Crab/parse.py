import re

with open("export.har", "r") as file:
    file_contents = file.read()

req_exp = re.findall(r'{\\"char\\":[0-9]{2}}', file_contents)

out_str = ""

for i in req_exp :
	out_str += chr(int(i[10:-1]))

out_str = out_str.replace(" ","_")

print(out_str[0:3].lower() + out_str[3:6] + "{" + out_str[7:-1] + "}")