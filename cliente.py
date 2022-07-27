import socket
import pickle


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

try:
    
    s.connect(('localhost', 9999))
    print("[1] para visualização de capacidade de armazenamento [2] para informações sobre redes/interfaces")
    while True:
        
        msg = input('Entre com a opção: ')
        
        s.send(msg.encode('ascii'))
                     
        if (msg == '@'):
            break
    
        if (msg == '1'):
            resp = s.recv(1024)
            
            
            andre = pickle.loads(resp)
            print(andre)
            
        if (msg[0] == '2'):
            resp = s.recv(1024)            
            
            andre = pickle.loads(resp)
            print(andre)
            
        
                
   
    s.close()
except Exception as erro:
    print(str(erro))
