inp = input()
a = inp.split()
new_one = '' 
new_two = ''
for i in range(len(list(a[0])) - 1, -1, -1):
    new_one += list(a[0])[i]
for i in range(len(list(a[1]))-1, -1, -1):
    new_two += list(a[1])[i]

# print(new_one, new_two)
if (int(new_one) >= int(new_two)): print(int(new_one))
else : print(int(new_two))
