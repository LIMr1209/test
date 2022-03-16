import base64
import os
import struct

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad


def encrypt_file(key, in_filename, out_filename=None, chunksize=64 * 1024):
    if not out_filename:
        out_filename = in_filename + '.enc'
    iv = os.urandom(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)
    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            # prefix = struct.pack('<Q', filesize)
            # outfile.write(prefix)
            outfile.write(iv)
            pos = 0
            while pos < filesize:
                chunk = infile.read(chunksize)
                pos += len(chunk)
                if pos == filesize:
                    chunk = pad(chunk, AES.block_size, style='pkcs7')
                outfile.write(encryptor.encrypt(chunk))


def decrypt_file(key, in_filename, out_filename=None, chunksize=64 * 1024):
    if not out_filename:
        out_filename = in_filename + '.dec'
    with open(in_filename, 'rb') as infile:
        # prefix = struct.unpack('<Q', infile.read(8))[0]
        iv = infile.read(16)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            encrypted_filesize = os.path.getsize(in_filename)
            pos = 16  # the filesize and IV.
            while pos < encrypted_filesize:
                chunk = infile.read(chunksize)
                pos += len(chunk)
                chunk = encryptor.decrypt(chunk)
                if pos == encrypted_filesize:
                    chunk = unpad(chunk, AES.block_size, style='pkcs7')
                outfile.write(chunk)


# encrypt_file(b'lizhenbinhhahaha', 'coffee_maker_001.glb', 'jia.glb')
# decrypt_file(b'lizhenbinhhahaha', 'jia.glb', 'jie.glb')

# key = b'1234567890123456'
# iv = b'abcdefghijklmnop'
# cipher = AES.new(key, AES.MODE_CBC, iv)
#
# text = b'secret text'
# padtext = pad(text, AES.block_size, style='pkcs7')
# cipherText = cipher.encrypt(padtext)
# print(padtext)
# encrypt_data = base64.b64encode(cipherText)
# print(encrypt_data)
#
# decrypter = AES.new(key, AES.MODE_CBC, iv)
# plaintext = decrypter.decrypt(cipherText)
# unpadtext = unpad(plaintext, AES.block_size, 'pkcs7')
# print(plaintext)
# print(unpadtext)

import re


def test(matched):
    if matched.group(1) is not None:
        return str(2)
#
#
s = 'zppt(8)479(1).ppt'
a = re.sub(r"\((\d+)\)\.", test, s)
print(a)


# replacement function to convert uppercase word to lowercase
# and lowercase word to uppercase
# def convert_case(match_obj):
#     if match_obj.group(1) is not None:
#         return match_obj.group(1).lower()
#     if match_obj.group(2) is not None:
#         return match_obj.group(2).upper()
#
# # Original String
# str = "EMMA loves PINEAPPLE dessert and COCONUT ice CREAM"
#
# # group 1 [A-Z]+ matches uppercase words
# # group 2 [a-z]+ matches lowercase words
# # pass replacement function 'convert_case' to re.sub()
# res_str = re.sub(r"([A-Z]+)|([a-z]+)", convert_case, str)
#
# # String after replacement
# print(res_str)
