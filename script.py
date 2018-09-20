from os import urandom
from Crypto.Util.number import bytes_to_long, long_to_bytes

username = raw_input('Your username>>').split('\0')[0] + 'admin'
password = raw_input('Your password>>')
s = username + '\0' + password + '\0'
final = s + str(urandom(255 - len(s)))
final = bytes_to_long(bytes(final))

if final % 2 == 0:
    final = final + 1

cookie = 1
print hex(final)
print hex(final**7)