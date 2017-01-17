cipher = "FQWGLOVHBPIJZRMEAKCYDSX|JGRMQOYGHMVBJWRWQFPWHGFFDQGFPFZRKBEEBJIZQQOCIBZKLFAFGQVFZFWWEOGWOPFGFHWOLPHLRLOLFDMFGQWBLWBWQOLKFWBYLBLYLFSFLJGRMQBOLWJVFPFWQVHQWFFPQOQVFPQOCFPOGFWFJIGFQVHLHLROQVFGWJVFPFOLFHGQVQVFILEOGQILHQFQGIQVVOSFAFGBWQVHQWIJVWJVFPFWHGFIWIHZZRQGBABHZQOCGFHX"
_plain = "eatnihgs    r          |"
print(cipher)

from collections import defaultdict

char_count = defaultdict(int)
for char in cipher:
  char_count[char] += 1
count_char = defaultdict(list)
for char, count in char_count.items():
  count_char[count].append(char)

for count in sorted(count_char.keys()):
  print(count, count_char[count])

key = {c: p for c, p in zip(cipher, _plain) if p != ' '}
plain = ''.join(key.get(char, ' ') for char in cipher)
print(cipher)
print(plain)


