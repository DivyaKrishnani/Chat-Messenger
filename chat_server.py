
import socket                                 #import libraries
import sys
import select

def send_msg(soc,message):                    #delivering messages to clients by taking it from host
    for socket in LIST:
        try:        
            if socket != server and socket != soc:   
                socket.send(message)
                
        except:
            socket.close()
            LIST.remove(socket)

LIST =[]
buff=4096
port=12345
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)         #server socket declaration
host=socket.gethostname()
print "host name : " 
print host
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((host,port))

server.listen(10)
LIST.append(server)               #adding server socket to list

print "SERVER STARTED ON PORT "  +str(port)
while 1:
    readable,writeable,error=select.select(LIST,[],[])
    for soc in readable:
        if soc == server:
            sockfd,addr = server.accept()
            LIST.append(sockfd)
            print "CLIENT (%s %s) IS CONNECTED" % addr
            send_msg(sockfd, "[%s:%s] JOINED CONVERSATION\n" % addr)
        else:
            try:
                data=soc.recv(buff)
                if data:
                    send_msg(soc, "\r" + '<' + str(soc.getpeername()) + '> ' + data)
            except:
                send_msg(soc, "CLIENT (%s, %s) IS OFFLINE" % addr)
	        print "CLIENT (%s, %s) IS OFFLINE" % addr
                soc.close()
                LIST.remove(soc)
                continue

server.close()



