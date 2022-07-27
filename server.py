import socket
import psutil
import pickle



socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
porta = 9999


socket_servidor.bind((host, porta))


socket_servidor.listen()
print("Servidor de arquivos ", host, "esperando conexão na porta", porta)


(socket_cliente,addr) = socket_servidor.accept()
print("Conectado a:", str(addr))

while True:
    
    msg = socket_cliente.recv(1024)
    
    msg_rec = msg.decode('ascii')
    
    lista = msg_rec.split()    
    resposta = 0
    
    try:
        if (lista[0] == '1'):
            total_disk = psutil.disk_usage('C:\\').total
            free_disk = psutil.disk_usage('C:\\').free          
            
            tupla_msg = ("armazenamento total:", total_disk/1024/1024/1024, "Armazenamento disponivel: ", free_disk/1024/1024/1024)            
            bytes_tupla = pickle.dumps(tupla_msg)
            socket_cliente.send(bytes_tupla)
            
        if (lista[0] == '2'):
            interfaces = psutil.net_if_addrs()
            nomes = []

            for i in interfaces:
                nomes.append(str(i))
            for i in nomes:
                print(i + ":")
                for j in interfaces[i]:
                    print("\t"+str(j))

            tupla_msg = (nomes, interfaces)            
            bytes_tupla = pickle.dumps(tupla_msg)
            socket_cliente.send(bytes_tupla)
             
        
        if (lista[0] == '@'):
            break
        
    except Exception as e:
        print('Argumento inválido')
        print(e)

socket_cliente.close()
socket_servidor.close()
        