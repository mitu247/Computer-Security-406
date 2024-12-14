import socket
import importlib
AES = importlib.import_module('1905086_f1')
ECDH = importlib.import_module('1905086_f2')
params = importlib.import_module('1905086_f5')

def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1"
    server_port = 12345
    server.bind((server_ip, server_port))
    server.listen(0)

    print(f"Listening on {server_ip} : {server_port}")

    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    x = params.receive_conv_int(client_socket)
    y = params.receive_conv_int(client_socket)
    a = params.receive_conv_int(client_socket)
    b = params.receive_conv_int(client_socket)
    p = params.receive_conv_int(client_socket)
    pubk_x = params.receive_conv_int(client_socket)
    pubk_y = params.receive_conv_int(client_socket)
    
    # print(x)
    # print(y)
    # print(a)
    # print(b)
    # print(p)
    # print(pubk_x)
    # print(pubk_y)
    
    pk_a = (pubk_x, pubk_y)
    G = (x, y)
    
    secret_b = params.get_random_num(p)
    pk_b_x, pk_b_y = ECDH.double_and_add_algo(G, secret_b, p, a)
    # print('Pk - b:', pk_b_x, pk_b_y)
    params.send(client_socket, pk_b_x)
    params.send(client_socket, pk_b_y)
    
    shared_key = ECDH.double_and_add_algo(pk_a, secret_b, p, a)
    
    session_key = shared_key[0]
    # print(session_key)
    rec_msg = client_socket.recv(1024).decode('utf-8')
    if rec_msg == "Alice: Ready for transmission":
        params.send(client_socket, "Bob: Ready for transmission")
        
    str_key = str(hex(session_key)[2:])
    len_s = len(hex(session_key)[2:])
    session_key_hex = []

    if len_s < 32:
        padlen = (32 - len_s)
        for i in range(padlen):
            str_key = '0' + str_key # Prepadding
            
    for i in range(16): # 16 bytes
        session_key_hex.append(str_key[i * 2 : (i * 2) + 2])
    
    # print(session_key_hex)
    roundkey_hexlist = AES.Round_Key_Generation(session_key_hex)
    
    text_iv = client_socket.recv(1024).decode('utf-8')
    ciphertext = client_socket.recv(1024).decode('utf-8')
    # print(iv, ciphertext)
    
    cipher_text_list = AES.Hex_Cov(ciphertext)
    iv = AES.Hex_Cov(text_iv)
    org_hexlist = AES.decryption(cipher_text_list,roundkey_hexlist,iv)
    
    org_text = AES.ascii_conv(org_hexlist)
    print("Received Message:", *org_text, sep = '')


    client_socket.close()
    print("Connection to client closed")
    server.close()


run_server()