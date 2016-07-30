from Crypto.Cipher import AES


def xor(xs, ys):  # xor bytes
  return ''.join(chr(x ^ y) for (x, y) in zip(xs, ys))


def inc_bytes(xs):
  xs = list(xs)
  for i in reversed(range(len(xs))):
    xs[i] = (xs[i] + 1) % 256
    if xs[i] > 0:
      break
  return bytes(xs)

def aes_cbc_decrypt(key, ctext):
  cipher = AES.AESCipher(key)
  c0 = ctext[:16]
  t = ''
  for i in range(16, len(ctext), 16):
    c1 = ctext[i: i + 16]
    d1 = cipher.decrypt(c1)
    t += xor(c0, d1)
    c0 = c1
  print(t[:-ord(t[-1])])

def aes_ctr_decrypt(key, ctext):
  cipher = AES.AESCipher(key)
  IV = ctext[:16]
  t = ''
  for i in range(16, len(ctext), 16):
    c1 = ctext[i: i + 16]
    d1 = cipher.encrypt(IV)
    t += xor(c1, d1)
    IV = inc_bytes(IV)
  print(t)

def solve():
  key = bytes.fromhex('140b41b22a29beb4061bda66b6747e14')
  ctext = bytes.fromhex('4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81')
  aes_cbc_decrypt(key, ctext)

  key = bytes.fromhex('140b41b22a29beb4061bda66b6747e14')
  ctext = bytes.fromhex('5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253')
  aes_cbc_decrypt(key, ctext)

  key = bytes.fromhex('36f18357be4dbd77f050515c73fcf9f2')
  ctext = bytes.fromhex('69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329')
  aes_ctr_decrypt(key, ctext)

  key = bytes.fromhex('36f18357be4dbd77f050515c73fcf9f2')
  ctext = bytes.fromhex('770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451')
  aes_ctr_decrypt(key, ctext)






if __name__ == '__main__':
  solve()







