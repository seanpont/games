
# Program 1
# x = int(raw_input('input number: '))
# if x % 2 == 0:
#     print 'Even'
# else:
#     print 'Odd'
# if x % 3 == 0:
#     print 'and divisible by 3'

# Program 2
# x = int(raw_input('enter integer: '))
# ans = 0
# while ans * ans * ans < abs(x):
#     ans = ans + 1
#     print ans
# if ans**3 != abs(x):
#     print '%d is not a perfect cube' % x
# else:
#     if x < 0:
#         ans = -ans
#     print 'cube root of %d is %d' % (x, ans)


# Program 3
# x = float(raw_input('enter integer: '))
# epsilon = 0.1
# numGuesses = 0
# ans = 0.0
# while abs(ans**2 - x) >= epsilon and ans <= x:
#     ans += 0.00001
#     numGuesses += 1
# print 'numGuesses =', numGuesses
# if abs(ans**2 - x) >= epsilon:
#     print 'Failed on square root of', x
# else:
#     print ans, 'is close to square root of', x


# Program 4
x = float(raw_input('enter integer: '))
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon and ans <= max(x, 1):
    print 'low %s high %s ans %s' % (low, high, ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print 'numGuesses =', numGuesses
print ans, 'is close to square root of', x












