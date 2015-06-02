sum = 0
for a in xrange(100000):
    if a % 3 == 0 or a % 5 == 0:
        sum = sum + a

print 'the final sum is', sum
