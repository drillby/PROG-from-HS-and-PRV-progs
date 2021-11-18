u = 78
u = int(u)

w = 58
w = int(w)

while w != 0:
    r = u % w
    r = int(r)
    u = w
    w = r
print(u)
