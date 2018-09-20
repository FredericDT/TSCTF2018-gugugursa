from Crypto import Random
from os import urandom
from Crypto.Util.number import bytes_to_long, long_to_bytes
from getmes import *


def main():
    flag = open('flag','r').readline()
    f = open('prime','r')
    p = int(f.readline(),16)
    q = int(f.readline(),16)
    n = p*q
    e = 7
    d = findModReverse(e,(p-1)*(q-1))
    #alarm(200)
    while True :
        choice = raw_input('Please [r]egister or [l]ogin :>>')
        if not choice :
            break;
        if choice[0] == 'r' :
            username = raw_input('Your username>>').split('\0')[0] + 'user'
            if len(username) == 0:
                break;
            password = raw_input('Your password>>')
            s = username + '\0' + password + '\0'
            if len(s) >= 128 :
                print "Too Long!!!"
                break
            final = s + urandom(255 - len(s))
            final = bytes_to_long(bytes(final))
            if final % 2 == 0:
                final = final + 1
            cookie = 1
            for i in range(e):
                cookie = (cookie * final) % n
                print 'Your Cookie>>',hex(cookie)[2:-1]
        if choice[0] == 'l' :
            cookie = raw_input('Give me your cookie>>')
            final = int(cookie,16)
            s = str(long_to_bytes(getmes(final, d, n)))
            username = s.split('\0')[0]
            if username[-4:] == 'user':
                print 'Hello',username[:-4]
            if username[-5:] == 'admin':
                print 'Hello admin',flag
                break;

if __name__ == '__main__':
    main()