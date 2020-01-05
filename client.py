import socket
import time
from collections import defaultdict

class Client:
    def __init__(self, host, port, timeout=2):
        self.host=host
        self.port=port
        self.timeout=timeout

    def parse_data(self,data):
        s = data.decode('utf8')
        dd = defaultdict(list)

        if s[0:2] == 'ok':
            if s[2:] == '\n\n':
                return {}
            d = s[2:].strip().split('\n')
            for i in d:
                ii = i.split()
                dd[ii[0]].append((int(ii[2]),float(ii[1])))

            return dict(dd)

        if s[0:5] == 'error':
            raise ClientError("wrong command")

    def get(self, key):
        s = "get "+key+"\n"
        with socket.create_connection((self.host, self.port),self.timeout) as sock:
            try:
                sock.sendall(s.encode("utf8"))
            except socket.timeout:
                print('send data timeout')
            
            except socket.error as ex:
                print('send data error',ex)

            while True:
                try:
                    data = sock.recv(1024)
                except socket.timeout:
                    print("close connection by timeout")
                    break
                except ClientError as e:
                    print(e.text)
                if not data:
                    break

                return self.parse_data(data)


    def put(self, key, value, timestamp=str(int(time.time()))):
       
        s = "put "+ key + " " + str(value) +" " + str(timestamp) + "\n"
        with socket.create_connection((self.host, self.port),self.timeout) as sock:
            try:
                sock.sendall(s.encode())
                data = sock.recv(1024).decode()
                if data == 'error\nwrong command\n\n':
                    raise ClientError()

            except socket.timeout:
                print('send data timeout')
            
            except socket.error as ex:
                print('send data error',ex)


class ClientError(Exception):
    def __init__(self, text):
        self.text = text
