
import socket
import string
import select
import sys


host = sys.argv[1]
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(2)

try:
    s.connect((host,port))
except:
    print 'FAILED TO CONNECT'
    sys.exit()

print 'CONNECTED YOU CAN START THE CONVERSATION'
sys.stdout.write('<ME>')
sys.stdout.flush()

while 1:
    stream=[sys.stdin,s]
    readable,writable,err=select.select(stream,[],[])
    for soc in readable:
        if soc == s:
            
            
            data = soc.recv(4096)
            if not data:
                print 'DISCONNECTED'
                sys.exit()
            else:
            
                sys.stdout.write(data)
                sys.stdout.write('<ME>')
                sys.stdout.flush()
        
        
        else:
            msg = sys.stdin.readline()
            s.send(msg)
            sys.stdout.write("<ME>")
            sys.stdout.flush()

