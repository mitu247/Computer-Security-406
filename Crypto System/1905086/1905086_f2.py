import random
import time

def bin_exp(a, b, m):
    res = 1
    while b > 0:
        if b & 1:
            res = (res * a)%m
        a = (a * a)%m
        b >>= 1
    return res

def add_points(point_P, point_Q,p,a):
    x1, y1 = point_P
    x2, y2 = point_Q
    #tangent line
    if point_P == point_Q:
        slope = (3 * x1 * x1 + a)*bin_exp(2*y1, p-2, p)
    else:
        slope = (y2 - y1)*bin_exp(x2-x1, p-2, p) #secant line

    x3 = (slope * slope - x1 - x2) % p
    y3 = (slope * (x1 - x3) - y1) % p
    target = (x3,y3)
    return target

def double_and_add_algo(G,k_a,p,a):
    k_a_bin = bin(k_a)[2:]
    result_point = G
    for current_bit in k_a_bin:
        # Double the result_point
        result_point = add_points(result_point,result_point,p,a)
        if current_bit == "1":
            # Add the base point G if the current bit is 1
            result_point = add_points(result_point,G,p,a)

    return result_point

def ECC(G,E,p,a):
    alice_elapsed_t = 0
    bob_elapsed_t = 0
    shrdkey_elapsed_t = 0
    for i in range(10):
        s_t = time.time()
        k_a = random.randint(2, E-1)
        A = double_and_add_algo(G, k_a, p, a)
        e_t = time.time()
        alice_elapsed_t+=(e_t - s_t)
        s_t = time.time()
        k_b = random.randint(2, E-1)
        B = double_and_add_algo(G,k_b,p,a)
        e_t = time.time()
        bob_elapsed_t += (e_t - s_t)
        s_t = time.time()
        r = double_and_add_algo(G,k_b*k_a,p,a)
        e_t = time.time()
        shrdkey_elapsed_t += (e_t - s_t)
    return (alice_elapsed_t/10,bob_elapsed_t/10,shrdkey_elapsed_t/10)
data = []
#128 bit key
p=0xfffffffdffffffffffffffffffffffff
a=0xfffffffdfffffffffffffffffffffffc
b=0xe87579c11079f43dd824993c2cee5ed3
G=(0x161ff7528b899b2d0c28607ca52c5b86, 0xcf5ac8395bafeb13c02da292dded7a83)
E=0xfffffffe0000000075a30d1b9038a115

#alice_elapsed_t,bob_elapsed_t,shrdkey_elapsed_t = ECC(G,E,p,a)
ret = ECC(G,E,p,a)
data.append([128, ret[0]*1000, ret[1]*1000, ret[2]*1000])
# 192 bit key
p = 0xfffffffffffffffffffffffffffffffeffffffffffffffff
a = 0xfffffffffffffffffffffffffffffffefffffffffffffffc
b = 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1
G = (0x188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012, 0x07192b95ffc8da78631011ed6b24cdd573f977a11e794811)
E = 0xffffffffffffffffffffffff99def836146bc9b1b4d22831

#alice_elapsed_t,bob_elapsed_t,shrdkey_elapsed_t = ECC(G,E,p,a)
ret = ECC(G,E,p,a)
data.append([192, ret[0]*1000, ret[1]*1000, ret[2]*1000])
# 256 bit key
p = 0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = 0xffffffff00000001000000000000000000000000fffffffffffffffffffffffc
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
G = (0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5)
E = 0xffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551

#alice_elapsed_t,bob_elapsed_t,shrdkey_elapsed_t = ECC(G,E,p,a)
ret = ECC(G,E,p,a)
data.append([256, ret[0]*1000, ret[1]*1000, ret[2]*1000])

headers = ["K  ", "    A     ", "    B     ", "  Shared Key  "]
format_str = "{:<3d} | {:<10.6f} | {:<10.6f} | {:<10.6f}"
if __name__ == "__main__":
    print(" | ".join(headers))
    print("-" * len(" | ".join(headers)))

for row in data:
    if __name__ == "__main__":
        print(format_str.format(*row))

