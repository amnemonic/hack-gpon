__author__ = "Adam Mnemonic"
__contact__ = "https://github.com/amnemonic"

import sys,os
import hmac


if len(sys.argv)!=2 or len(sys.argv[1])!=12: print('Usage: {0} <serial_no>\nFor example:\n  {0} ALCL1234ABCD\n'.format(os.path.basename(sys.argv[0]))); exit(1)

ont_login = "ONTUSER"
ont_serial = sys.argv[1][:4] + sys.argv[1][4:].lower()


def calculate_ont_password(username, serialno):
    hmkey1 = "01 03 0A 10 13 05 17 64 C8 06 14 19 B4 9D 05 00"
    hmkey2 = "05 11 3A 60 7B FB 0F 43 5C 21 BE 86 41 32 1C 00"
    alphabet = "2345679abcdefghijkmnpqrstuvwxyzACDEFGHJKLMNPQRSTUVWXYZ"
    payload = '{}-{}'.format(serialno,username).encode()
    md5hmac = hmac.new(bytes.fromhex(hmkey1), payload, 'MD5').digest()

    password = ""
    for i in range(len(md5hmac)):
        password += alphabet[md5hmac[i]%54]
    return password


if __name__ == '__main__':
    print('Device serial:', ont_serial)
    print('User name    :', ont_login)
    print('Password     :', calculate_ont_password(ont_login,ont_serial))
