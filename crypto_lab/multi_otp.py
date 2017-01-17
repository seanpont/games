import string

ciphers = [
  'BB3A65F6F0034FA957F6A767699CE7FABA855AFB4F2B520AEAD612944A801E',
  'BA7F24F2A35357A05CB8A16762C5A6AAAC924AE6447F0608A3D11388569A1E',
  'A67261BBB30651BA5CF6BA297ED0E7B4E9894AA95E300247F0C0028F409A1E',
  'A57261F5F0004BA74CF4AA2979D9A6B7AC854DA95E305203EC8515954C9D0F',
  'BB3A70F3B91D48E84DF0AB702ECFEEB5BC8C5DA94C301E0BECD241954C831E',
  'A6726DE8F01A50E849EDBC6C7C9CF2B2A88E19FD423E0647ECCB04DD4C9D1E',
  'BC7570BBBF1D46E85AF9AA6C7A9CEFA9E9825CFD5E3A0047F7CD009305A71E'
]

ciphers = [bytes.fromhex(c) for c in ciphers]

accepted_chars = string.ascii_letters + ' .,!?()'
possible_keys = []

for col in range(31):
  key_list = []
  for k in range(256):
    cipher_chars = [k ^ cipher[col] for cipher in ciphers]
    if all(chr(c) in accepted_chars for c in cipher_chars):
      key_list.append(k)
  possible_keys.append(key_list)

chars = ' etaoinshrdlc,.umwfgypbvkjxqz!?()'
denom = len(chars)
def score_of(char):
  char = char.lower()
  if char not in chars:
    raise Exception(char + ' not in chars')
  return len(chars) - chars.index(char)


key = []
for i, pk in enumerate(possible_keys):
  # pick the most probable key
  max_key, max_score = 0, 0
  for k in pk:
    score = sum([score_of(chr(k ^ cipher[i])) for cipher in ciphers])
    print(i, k, score)
    if score > max_score:
      max_key, max_score = k, score
  key.append(max_key)

print(key)
for cipher in ciphers:
  print(''.join(chr(k ^ c) for k, c in zip(key, cipher)))



