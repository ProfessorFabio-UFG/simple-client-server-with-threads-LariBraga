from threading import Thread
from socket  import *
from constCS import * 

def calcula(conn, addr):
    try:
        while True:
            data = conn.recv(1024) # receive data from client
            if not data: break # stop if client stopped
                
            conta = bytes.decode(data) # recebe os dados do cliente decodificados para string
            valores = conta.split(' ') # separa cada elemento da entrada com um espaço entre, criando um lista com esses elementos
            # valores[0] = primeiro número
            # valores[1] = segundo número
            # valores[2] = operação (add, sub ou mult)
            
            # convertendo os números de string para float
            n1 = int(valores[0]) 
            n2 = int(valores[1])
                
            # verificando a operação
            if valores[2] == 'add':
                resultado = n1 + n2
            elif valores[2] == 'sub':
                resultado = n1 - n2
            elif valores[2] == 'mult':
                resultado = n1 * n2
                
            conn.send(str.encode(str(resultado))) # retorna o resultado da operação para o cliente
    finally:
        conn.close()

    
if __name__ == '__main__': 
    s = socket(AF_INET, SOCK_STREAM) 
    s.bind((HOST, PORT)) 
    s.listen()
    
    while True: # forever
        try:
            (conn, addr) = s.accept()  # returns new socket and addr. client
            cliente = Thread(target=calcula, args=(conn, addr))
            cliente.start()
        finally:
            break
    
    s.close()