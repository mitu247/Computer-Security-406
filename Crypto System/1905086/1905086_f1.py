import time
import string
import random
import numpy as np
from BitVector import *
import sys
sys.stdin = open('inp.txt', 'r')

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)
InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)
Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]
InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]
rc = []
const = 0x01
rc.append(hex(const)[2:])
for i in range(2, 11):
    if (const < 0x80):
        const = 2 * const
    else:
        const = (2 * const) ^ 0x11B
    rc.append(hex(const)[2:])

def add_IV_plaintext(A,B):
    gen_list = []
    for (s, w) in zip(A,B):
        bv1 = BitVector(hexstring=str(s))
        bv2 = BitVector(hexstring=str(w))
        bv3 = bv1 ^ bv2
        gen_list.append(bv3.get_bitvector_in_hex())
    return gen_list

def iv_generator(chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(16))

def Hex_Cov(string,isKey = False):
    hexlist = []
    strlen = len(string)
    padlen = 0
    if (strlen % 16 != 0):
        padlen = 16 - strlen % 16

    for s in string:
        hexlist.append(BitVector(intVal=ord(s), size=8).get_bitvector_in_hex())

    for i in range(padlen):
        hexlist.append('00')

    if isKey:
        return hexlist[0:16]
    else:
        return hexlist


def func_g(roundkey, pos):
    new_w = []
    new_arr = roundkey[pos * 4:]
    new_arr = np.roll(new_arr,-1)
    for s in new_arr:
        bv = BitVector(hexstring=s).intValue()
        subval = Sbox[bv]
        subval = BitVector(intVal=subval, size=8)
        new_w.append(subval.get_bitvector_in_hex())
    bv_r = BitVector(hexstring=rc[pos//4]) ^ BitVector(hexstring=new_w[0])
    new_w[0] = bv_r.get_bitvector_in_hex()
    return new_w


def matrix_multiply(A):
    result = [[0 for i in range(4)] for j in range(4)]
    AES_modulus = BitVector(bitstring='100011011')
    for ix in range(4):
        for iy in range(4):
            dot_product = BitVector(hexstring = '00')
            for k in range(4):
                bv1 = BitVector(hexstring = str(A[k][iy]))
                bv2 = Mixer[ix][k]
                dot_product = dot_product ^ (bv1.gf_multiply_modular(bv2, AES_modulus, 8))
            result[ix][iy] = dot_product.get_bitvector_in_hex()
    return result

def matrix_inv_multiply(A):
    result = [[0 for i in range(4)] for j in range(4)]
    AES_modulus = BitVector(bitstring='100011011')
    for ix in range(4):
        for iy in range(4):
            dot_product = BitVector(hexstring = '00')
            for k in range(4):
                bv1 = BitVector(hexstring = str(A[k][iy]))
                bv2 = InvMixer[ix][k]
                dot_product = dot_product ^ (bv1.gf_multiply_modular(bv2, AES_modulus, 8))
            result[ix][iy] = dot_product.get_bitvector_in_hex()
    return result

def add_round_key(A,B):
    state_mat = [[0 for i in range(4)] for j in range(4)]
    # state_mat = np.zeros(16, dtype=str).reshape(4,4)
    for ix in range(4):
        for iy in range(4):
            bv1 = BitVector(hexstring=A[ix][iy])
            bv2 = BitVector(hexstring=B[ix][iy])
            bv3 = bv1 ^ bv2
            state_mat[ix][iy] = bv3.get_bitvector_in_hex()
    return state_mat

def subs_sbox(state_mat):
    for ix in range(4):
        for iy in range(4):
            bv = BitVector(hexstring=state_mat[ix][iy]).intValue()
            subval = Sbox[bv]
            subval = BitVector(intVal=subval, size=8)
            state_mat[ix][iy] = subval.get_bitvector_in_hex()
    return state_mat

def subs_inv_sbox(state_mat):
    for ix in range(4):
        for iy in range(4):
            bv = BitVector(hexstring=state_mat[ix][iy]).intValue()
            subval = InvSbox[bv]
            subval = BitVector(intVal=subval, size=8)
            state_mat[ix][iy] = subval.get_bitvector_in_hex()
    return state_mat

def Round_Key_Generation(hexlist):
    for roundkey in range(1, 11):
        new_w = func_g(hexlist, (roundkey * 4) - 1)
        for s, w in zip(new_w, hexlist[((roundkey - 1) * 16): ((roundkey - 1) * 16) + 4]):
            bv1 = BitVector(hexstring=s)
            bv2 = BitVector(hexstring=w)
            bv3 = bv1 ^ bv2
            hexlist.append(bv3.get_bitvector_in_hex())

        for i in range(roundkey * 4, (roundkey * 4) + 3):
            for j in range(4):
                (s, w) = (hexlist[i * 4 + j], hexlist[(i - 3) * 4 + j])
                bv1 = BitVector(hexstring=s)
                bv2 = BitVector(hexstring=w)
                bv3 = bv1 ^ bv2
                hexlist.append(bv3.get_bitvector_in_hex())
    return hexlist

def encryption(plain_text_list, hexlist, iv):
    ciphertext = []
    for i in range(0, len(plain_text_list), 16):
        plain = add_IV_plaintext(plain_text_list[i:i+16],iv)

        plain_2d = np.reshape(plain, (4, 4))
        plain_matrix = np.transpose(plain_2d)
        matrix_2d = np.reshape(hexlist[0:16], (4, 4))
        key_matrix = np.transpose(matrix_2d)
        state_mat = add_round_key(plain_matrix, key_matrix)
        for j in range(16, len(hexlist) - 16, 16):
            state_mat = subs_sbox(state_mat)
            for k in range(4):
                state_mat[k] = np.roll(state_mat[k], -k)
            state_mat = matrix_multiply(state_mat)

            matrix_2d = np.reshape(hexlist[j:j + 16], (4, 4))
            key_matrix = np.transpose(matrix_2d)
            state_mat = add_round_key(state_mat, key_matrix)
        #last round
        state_mat = subs_sbox(state_mat)
        for k in range(4):
            state_mat[k] = np.roll(state_mat[k], -k)
        matrix_2d = np.reshape(hexlist[-16:], (4, 4))
        key_matrix = np.transpose(matrix_2d)
        state_mat = add_round_key(state_mat, key_matrix)
        for col in range(4):
            for row in range(4):
                ciphertext.append(state_mat[row][col])

        iv = ciphertext[i:i+16]
    return ciphertext

def decryption(cipher_text_list,hexlist,iv):
    plain_text = []
    for i in range(0, len(cipher_text_list), 16):
        plain_2d = np.reshape(cipher_text_list[i:i+16], (4, 4))
        plain_matrix = np.transpose(plain_2d)
        matrix_2d = np.reshape(hexlist[-16:], (4, 4))
        key_matrix = np.transpose(matrix_2d)
        state_mat = add_round_key(plain_matrix, key_matrix)
        for j in range(1,10):
            for k in range(4):
                state_mat[k] = np.roll(state_mat[k], k)
            state_mat = subs_inv_sbox(state_mat)
            matrix_2d = np.reshape(hexlist[-16*(j+1):-16*j], (4, 4))
            key_matrix = np.transpose(matrix_2d)
            state_mat = add_round_key(state_mat, key_matrix)
            state_mat = matrix_inv_multiply(state_mat)
        for k in range(4):
            state_mat[k] = np.roll(state_mat[k], k)
        state_mat = subs_inv_sbox(state_mat)
        matrix_2d = np.reshape(hexlist[0:16], (4, 4))
        key_matrix = np.transpose(matrix_2d)
        state_mat = add_round_key(state_mat, key_matrix)
        for col in range(4):
            for row in range(4):
                plain_text.append(state_mat[row][col])

        plain_text[i:i+16] = add_IV_plaintext(plain_text[i:i+16],iv)
        iv = cipher_text_list[i:i+16]
    return plain_text

def ascii_conv(hextext):
    chipher_ascii = []
    for s in hextext:
        b = BitVector(hexstring=s).intValue()
        chipher_ascii.append(chr(b))
    return chipher_ascii

if __name__ == "__main__":
    string = input()

    print('Key:')
    print('In ASCII: ',string)
    hexlist = Hex_Cov(string,True)

    print("In HEX: ",*hexlist,sep = ' ')

    plain_text = input()

    print('\nPlain Text:')
    print('In ASCII:', plain_text)
    plain_text_list = Hex_Cov(plain_text)

    print("In HEX: ",*plain_text_list,sep=' ')
    sk_t = time.time()
    hexlist = Round_Key_Generation(hexlist)
    ek_t = time.time()

    iv = Hex_Cov(iv_generator())

    se_t = time.time()
    ciphertext = encryption(plain_text_list,hexlist,iv)
    ee_t = time.time()


    print('\nCiphered Text: ')
    print('In HEX: ',*ciphertext,' ')

    chipher_ascii = ascii_conv(ciphertext)

    print('In ASCII: ',*chipher_ascii, sep='')
    sd_t = time.time()
    cipher = decryption(ciphertext,hexlist,iv)
    ed_t = time.time()

    print('\nDeciphered Text: ')
    print('In HEX: ',*cipher,' ')

    org_text = ascii_conv(cipher)

    print('In ASCII: ',*org_text, sep='')
    print('\nExecution Time Details: ')
    print('Key Schedule Time: ',(ek_t-sk_t)*1000,'ms')
    print('Encryption Time: ',(ee_t-se_t)*1000,'ms')
    print('Decryption Time: ',(ed_t-sd_t)*1000,'ms')
# for i in range(0, len(hexlist), 16):
#     print('Round key -', i // 16)
#     print(*hexlist[i: i + 16], sep=' ')

