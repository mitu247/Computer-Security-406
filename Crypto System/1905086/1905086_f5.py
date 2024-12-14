# Generating ECDH parameters
import importlib
import math
powalt = importlib.import_module('1905086_f2')
import sympy
import random
import time

def get_params(nbits):
    p = sympy.randprime(2**(nbits-1), 2**(nbits) - 1)
    a = random.getrandbits(nbits)
    x = random.getrandbits(nbits)
    y = random.getrandbits(nbits)
    b = ( powalt.bin_exp(y, 2, p) - powalt.bin_exp(x, 3, p) - ( a * x ) ) % p
    # print((4*powalt.bin_exp(a, 3, p) + 27*powalt.bin_exp(b, 2, p)) % p)
    

    while ( (4*powalt.bin_exp(a, 3, p) + 27*powalt.bin_exp(b, 2, p)) % p == 0 ):
        x = random.getrandbits(nbits)
        y = random.getrandbits(nbits)
        b = ( powalt.bin_exp(y, 2, p) - powalt.bin_exp(x, 3, p) - ( a * x ) ) % p
    
    return (x, y, a, b, p)

def get_random_num(p):
    return random.randint(2,math.sqrt(p))

def send(c, data): #datastring
    datastring = str(data)
    time.sleep(0.01)
    c.sendall(datastring.encode())
    
def receive_conv_int(c):
    return int(c.recv(1024).decode("utf-8"))
