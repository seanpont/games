from Crypto.Hash import SHA256
import os

fname = '/Users/seanpont/Downloads/6.1.intro.mp4_download'
fsize = os.path.getsize(fname)
f = open(fname, 'rb')
print('file size: %s' % fsize)
start = (fsize // 1024) * 1024
if start == fsize:
  start -= 1024
h = SHA256.new()
last_hash = bytes()
for offset in range(start, -1, -1024):
  f.seek(offset, 0)
  bs = f.read(1024)
  next_hash = SHA256.new(data=bs)
  next_hash.update(last_hash)
  last_hash = next_hash.digest()
  print(offset, bytes(last_hash).hex())

