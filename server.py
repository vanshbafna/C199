import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = '127.0.0.1'
port = 8000
server.bind((ip_address, port))
server.listen()
list_of_clients = []
print("Server has started...")