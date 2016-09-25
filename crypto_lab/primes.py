def gcd(a, b):
  return max([x for x in range(1, min(a, b) + 1) if a % x == 0 and b % x == 0])

def phi(a):
  return len([x for x in range(1, a) if gcd(x, a) == 1])

print gcd(12, 16)
print phi(12)

p, q, r = 7, 11, 13
print phi(p*q*r)
print (p-1)*(q-1)*(r-1)
