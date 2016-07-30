

f1 = lambda x: (x + 1) % 64
f2 = lambda x: (x * 2) % 64
f3 = lambda x: (x * 3 + 1) % 64
f4 = lambda x: 0

feistel = lambda f, r, l: (f(r) ^ l, r)

print feistel(f1, 12, 8)




