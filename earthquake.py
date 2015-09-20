
# from random import random
#
# p1 = .0123
# cost = 800000
# premium = 3000
# deductable = 50000
# fund = 0
#
# balances = []
# for _ in xrange(100000):
#     fund = 0
#     balance = 0
#     for year in xrange(30):
#         fund = fund * 1.05 + premium
#         if random() < p1:  # earthquake hits
#             damage = cost * (1 if random() < .5 else 0)
#             balance += damage - deductable
#             break
#     balances.append(balance)
#
# print sum(balances) / float(len(balances))


r = 1.05

print 3000 * r**30 - 3000
print sum([r**y for y in xrange(1, 31)]) * 3000 - 3000*30 - 91000
print [y for y in xrange(1, 31)]








