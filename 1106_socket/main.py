import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('172.29.11.136',80))
ipaddress = s.getsockname()[0]
print(ipaddress)