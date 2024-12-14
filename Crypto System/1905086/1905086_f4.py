import socket
import importlib
import time
AES = importlib.import_module('1905086_f1')
ECDH = importlib.import_module('1905086_f2')
params = importlib.import_module('1905086_f5')

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"
    server_port = 12345

    client.connect((server_ip, server_port))

    # Alice
    (x, y, a, b, p) = params.get_params(192)
    
    # double_and_add_algo(G,k_a,p,a)
    secret_a = params.get_random_num(p)
    public_a_x, public_a_y = ECDH.double_and_add_algo((x, y), secret_a, p, a)
    
    params.send(client, x)
    params.send(client, y)
    params.send(client, a)
    params.send(client, b)
    params.send(client, p)
    params.send(client, public_a_x)
    params.send(client, public_a_y)
    
    # print(x)
    # print(y)
    # print(a)
    # print(b)
    # print(p)
    # print(public_a_x)
    # print(public_a_y)
    
    pk_b_x = params.receive_conv_int(client)
    pk_b_y = params.receive_conv_int(client)
    # print(pk_b_x)
    # print(pk_b_y)
    
    pk_b = (pk_b_x, pk_b_y)
    shared_key = ECDH.double_and_add_algo(pk_b, secret_a, p, a)
    
    session_key = shared_key[0]
    # print(shared_key)
    
    params.send(client, "Alice: Ready for transmission")
    
    rec_msg = client.recv(1024).decode('utf-8')
    if rec_msg == "Bob: Ready for transmission":
        print("Tranmission starting...")
        
    # print(hex(session_key)[2:])
    str_key = str(hex(session_key)[2:])
    len_s = len(hex(session_key)[2:])
    session_key_hex = []

    if len_s < 32:
        padlen = (32 - len_s)
        for i in range(padlen):
            str_key = '0' + str_key # Prepadding
            
    for i in range(16): # 16 bytes
        session_key_hex.append(str_key[i * 2 : (i * 2) + 2])
    
    roundkey_hexlist = AES.Round_Key_Generation(session_key_hex)
    text_iv = AES.iv_generator()
    iv = AES.Hex_Cov(text_iv)
    
    # Sending encrypted message
    plain_text = "Two One Nine Two"
    plain_text_list = AES.Hex_Cov(plain_text)
    ciphertext = AES.encryption(plain_text_list,roundkey_hexlist,iv)
    cipher_ascii = ''
    for c in AES.ascii_conv(ciphertext):
        cipher_ascii = cipher_ascii + c
    
    params.send(client, text_iv) # Send the iv explicitly
    params.send(client, cipher_ascii)
    
    print(iv, cipher_ascii)

    client.close()
    print("Connection to server closed")

run_client()
