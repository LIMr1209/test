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
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)
            pos = 0
            while pos < filesize:
                chunk = infile.read(chunksize)
                pos += len(chunk)
                if pos == filesize:
                    chunk = pad(chunk, AES.block_size)
                outfile.write(encryptor.encrypt(chunk))


def decrypt_file(key, in_filename, out_filename=None, chunksize=64 * 1024):
    if not out_filename:
        out_filename = in_filename + '.dec'
    with open(in_filename, 'rb') as infile:
        filesize = struct.unpack('<Q', infile.read(8))[0]
        iv = infile.read(16)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            encrypted_filesize = os.path.getsize(in_filename)
            pos = 8 + 16  # the filesize and IV.
            while pos < encrypted_filesize:
                chunk = infile.read(chunksize)
                pos += len(chunk)
                chunk = encryptor.decrypt(chunk)
                if pos == encrypted_filesize:
                    chunk = unpad(chunk, AES.block_size)
                outfile.write(chunk)


# encrypt_file(b'lizhenbinhhahaha', 'coffee_maker_001.glb', 'jia.glb')
decrypt_file(b'lizhenbinhhahaha', 'jia.glb', 'jie.glb')

#
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad
# from Crypto.Util.Padding import unpad
#
# key = b'1234567890123456'
# iv = b'abcdefghijklmnop'
# cipher = AES.new(key, AES.MODE_CBC, iv)
#
# text = b'secret text'
# padtext = pad(text, 16, style='pkcs7')
# cipherText = cipher.encrypt(padtext)
# print(padtext)
# print(cipherText)
#
# decrypter = AES.new(key, AES.MODE_CBC, iv)
# plaintext = decrypter.decrypt(cipherText)
# unpadtext = unpad(plaintext, 16, 'pkcs7')
# print(plaintext)
# print(unpadtext)
