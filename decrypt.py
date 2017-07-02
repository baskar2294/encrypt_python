from Crypto.Cipher import AES
import base64
import os

# the block size for the cipher object; must be 16 per FIPS-197
BLOCK_SIZE = 16

# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'

# one-liner to sufficiently pad the text to be encrypted


def pad(s): return s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING

# one-liners to encrypt/encode and decrypt/decode a string
# encrypt with AES, encode with base64


def EncodeAES(c, s): return base64.b64encode(c.encrypt(pad(s)))


def DecodeAES(c, e): return c.decrypt(base64.b64decode(e)).rstrip(PADDING)


# generate a random secret key
secret = os.urandom(BLOCK_SIZE)

# create a cipher object using the random secret
cipher = AES.new('baskarencryptiontechniquehacked.')


import io
import os
dirpath = "G:\\file\\file\\"
files = os.listdir("G:\\file\\file\\encrypt\\")
if not os.path.exists(dirpath+"decrypt"):
    os.makedirs(dirpath+"decrypt")
for file in files:
    if file.find('.') == -1:
        continue
    else:
        with open(dirpath + "encrypt\\" + file, 'rb') as inf:
            jpgdata = inf.read()        
        decoded = DecodeAES(cipher, jpgdata)
        with open(dirpath + "decrypt\\" + file, 'wb') as inf:
            jpgdata = inf.write(decoded)