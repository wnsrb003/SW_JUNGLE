import math
inp = input()
a = int(inp.split()[0])
b = int(inp.split()[1])
v = int(inp.split()[2])

print(math.ceil((v-b) / (a-b)))

