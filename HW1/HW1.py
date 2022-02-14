#!/usr/bin/env python3

import sys
import traceback
import Crypto.Cipher
# BEGIN SOLUTION
# please import only standard modules and make sure that your code compiles and runs without unhandled exceptions 
from Crypto.Cipher import AES
# END SOLUTION

def problem_1():
    with open("cipher1.bin", "rb") as cipher_file:
        cipher_text = cipher_file.read()

    # BEGIN SOLUTION
    ivkey = bytes([0] * 16)
    key = bytearray(b'')
    for i in range(16):
        if i % 2 == 1:
            key.append(2)
        else:
            key.append(1)
    cipher = AES.new(key, AES.MODE_CBC, iv=ivkey)
    plain_text = cipher.decrypt(cipher_text)
    # END SOLUTION

    with open("plain1.txt", "wb") as plain_file:
        plain_file.write(plain_text)


def problem_2():
    with open("cipher2.bin", "rb") as cipher_file:
        cipher_text = cipher_file.read()

    # BEGIN SOLUTION
    modified_cipher_text = bytearray(b'')
    for i in range(16):
        modified_cipher_text.append(cipher_text[i+16])
    for i in range(16, 32):
        modified_cipher_text.append(cipher_text[i-16])
    for i in range(32, len(cipher_text)):
        modified_cipher_text.append(cipher_text[i])
    
    ivkey = bytes([0] * 16)
    key = bytearray(b'')
    for i in range(16):
        if i % 2 == 1:
            key.append(2)
        else:
            key.append(1)
    cipher = AES.new(key, AES.MODE_CBC, iv=ivkey)
    plain_text = cipher.decrypt(modified_cipher_text)
    # END SOLUTION

    with open("plain2.txt", "wb") as plain_file:
        plain_file.write(plain_text)


def problem_3():
    with open("cipher3.bmp", "rb") as cipher_file:
        cipher_bmp = cipher_file.read()
    with open("msg3.bmp", "rb") as message_file:
        other_bmp = message_file.read()

    # BEGIN SOLUTION
    modified_cipher_bmp = bytearray(cipher_bmp)
    for i in range(1000):
        modified_cipher_bmp[i] = other_bmp[i]
    # END SOLUTION

    with open("cipher3_modified.bmp", "wb") as modified_cipher_file:
        modified_cipher_file.write(modified_cipher_bmp)


def problem_4():
    with open("plain4A.txt", "rb") as plain_file:
        plain_text_a = plain_file.read()
    with open("cipher4A.bin", "rb") as cipher_file:
        cipher_text_a = cipher_file.read()
    with open("cipher4B.bin", "rb") as cipher_file:
        cipher_text_b = cipher_file.read()

    # BEGIN SOLUTION
    plain_text_b = cipher_text_b
    # END SOLUTION

    with open("plain4B.txt", "wb") as plain_file:
        plain_file.write(plain_text_b)


def problem_5():
    with open("cipher5.bin", "rb") as cipher_file:
        cipher_text = cipher_file.read()

    # BEGIN SOLUTION
    plain_text = cipher_text
    key = bytes([0] * 16)
    # END SOLUTION

    with open("plain5.txt", "wb") as plain_file:
        plain_file.write(plain_text)


def main():
    try:
        problem_1()
        problem_2()
        problem_3()
        problem_4()
        problem_5()
    except Exception:
        print("Exception:")
        traceback.print_exc(file=sys.stdout)


if __name__ == "__main__":
    main()
