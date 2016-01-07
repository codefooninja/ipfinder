
import socket

hostnames = [
'Dgold-Dev',
'gmail.com'
]

for hostname in hostnames:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect((hostname,80))
    print(hostname +' --> '+s.getsockname()[0])
    s.close
