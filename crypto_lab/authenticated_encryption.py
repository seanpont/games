from urllib import request

TARGET = 'http://crypto-class.appspot.com/po?er='

def query(q):
  target = TARGET + request.quote(q)  # Create query URL
  try:
    request.urlopen(target)  # Send HTTP request to server
  except request.HTTPError as e:
    return e.code == 404  # good padding

'The Magic Words are Squeamish Ossifrage'
'sO hsimaeuqS era'
'sifrage\t\t\t\t\t\t\t\t\t'

def attack():
  c = bytearray.fromhex('f20bdba6ff29eed7b046d1df9fb7000058b1ffb4210a580f748b4ac714c001bd4a61044426fb515dad3f21f18aa577c0bdf302936266926ff37dbf7035d5eeb4')
  c1, c2, c3, c4 = (c[i:i + 16] for i in range(0, 64, 16))

  # d2_solution = bytearray(16)
  # for i in range(1, 17):
  #   found_solution = False
  #   for x in range(0, 255):
  #     d1 = c1[:]
  #     for j in range(1, i):
  #       d1[-j] ^= d2_solution[-j] ^ i
  #     d1[-i] ^= x ^ i
  #     d = d1 + c2
  #     if query(d.hex()):
  #       d2_solution[-i] = x
  #       found_solution = True
  #       break
  #   if not found_solution:
  #     print('\nfailed to find solution at byte', i)
  #     return
  # print(d2_solution)

  d3_solution = bytearray(16)
  for i in range(1, 17):
    found_solution = False
    for x in range(0, 255):
      d2 = c2[:]
      for j in range(1, i):
        d2[-j] ^= d3_solution[-j] ^ i
      d2[-i] ^= x ^ i
      d = c1 + d2 + c3
      if query(d.hex()):
        d3_solution[-i] = x
        found_solution = True
        break
    if not found_solution:
      print('\nfailed to find solution at byte', i)
      return
  print(d3_solution)

  d4_solution = bytearray(16)
  for i in range(1, 17):
    found_solution = False
    for x in range(0, 255):
      d3 = c2[:]
      for j in range(1, i):
        d3[-j] ^= d4_solution[-j] ^ i
      d3[-i] ^= x ^ i
      d = c1 + c2 + d3 + c4
      if query(d.hex()):
        d4_solution[-i] = x
        found_solution = True
        break
    if not found_solution:
      print('\nfailed to find solution at byte', i)
      return
  print(d4_solution)



attack()