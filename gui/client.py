from socket import socket, error, gaierror, AF_INET, SOCK_STREAM, gethostbyname
import sys
import time


class Client:
    def __init__(self):
        self.host = "localhost"
        self.port = 3000
        self.s = None

    def connect(self):
        try:
            self.s = socket(AF_INET, SOCK_STREAM)
        except error:
            print("Error al crear el socket")
            sys.exit()

        print("Obteniendo dir ip")
        try:
            remote_ip = gethostbyname(self.host)
        except gaierror:
            print("Error, direccion no encontrada")
            sys.exit()

        # Conectandose al sistema
        print(f"Conectandose al servidor {self.host} en el puerto {self.port}")
        self.s.connect((remote_ip, self.port))

    def query(self, elem):
        #    emoji = bytes([0xF0, 0x9F ,0xA4 ,0xA3])
        query = bytearray(f"{elem}\n", "UTF8")  # dos lineas
        # query.append(13)
        try:
            self.s.sendall(query)
        except error:
            print("Error de comunicacion")
        # Se aumento el buffer
        reply = self.s.recv(10240)
        print(f"Lei {reply}")
        reply = reply.decode()
        # while not '\n' in reply:
        #     res = self.s.recv(256)
        #     reply = reply + res.decode()
        return reply

    def close(self):
        self.s.close()
        print("Eso es todo")
