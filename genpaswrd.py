import random
plen = int(input("enter the length of password:"))
m="abcdefghijklmnopqrstuvwxyz$%#*()!+=@_?"
p = "".join(random.sample(m,plen))
print(p)