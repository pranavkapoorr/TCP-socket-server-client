import socket as S
import threading

class serverTCP():
    #initializes socket
    s = S.socket(S.AF_INET, S.SOCK_STREAM)
    #is the classBoolean to check states of connection
    closeNow = False

    def __init__(self,serverIp,Port):
        self.s.bind((serverIp,Port))
        self.s.listen()
        print("waiting for a connections at ",serverIp+":",Port) 
        self.acceptConnections()
        
    def acceptConnections(self):
        while True:
            connection,client_address = self.s.accept()
            print('connection from', client_address)
            self.startThreads(connection)
            
        
        # Receive the data in small chunks and retransmit it
       
    """receive function prints the incoming message on console"""    
    def receive(self,connection):
        while True:
            msg = connection.recv(1024)
            x = msg.decode('ascii')
            print("RECEIVEED from",connection.getpeername() ,">",x)
            if x == "bye" or x == "Bye" or x == "BYE":
                connection.close()
                return
            elif x == "END":
                self.closeNow = True
                print("closing server")
                self.closeSocket()
                return
    
    """send function takes input from user from console and sends it through tcp socket connection"""            
    def send(self,connection):
        while True:
            msg = input()
            if self.closeNow == False:
                msgToSend = bytearray()
                li = [ord(c) for c in msg]
                for c in li:
                    msgToSend.append(c)
                connection.send(msgToSend)
                print("SENT to",connection.getpeername(),">",msgToSend.decode())
            else:
                print("couldn't send the message as Connection Closed...")
                return
    
    """startThreads starts 2 threads one for receiving and one for sending"""        
    def startThreads(self,connection):
        threads = []
        t1 = threading.Thread(target=self.send,args=(connection,))
        threads.append(t1)
        t2 = threading.Thread(target=self.receive,args=(connection,))
        threads.append(t2)
        t1.start()
        t2.start()
        
    """closes the socket"""   
    def closeSocket(self):
        self.s.close()
        
#creating object of the class leading to connecting to specified socket address
socket = serverTCP("xxx.xxx.xxx.xxx",0000)
