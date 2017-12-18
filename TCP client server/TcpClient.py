import socket as S
import threading

"""clientTCP class is a simple multithreaded tcp socket client which takes in host ip as string and port as integer"""
class clientTCP():
    #initializes socket
    s = S.socket(S.AF_INET, S.SOCK_STREAM)
    #is the classBoolean to check states of connection
    closeNow = False
    
    """constructor takes input hostaddress and port, connects to it and starts reading and writing threads"""
    def __init__(self,host,port):
        host = host                     
        port = port
        self.s.connect((host, port))
        self.startThreads()
        
    """receive function prints the incoming message on console"""    
    def receive(self):
        while True:
            msg = self.s.recv(1024)
            x = msg.decode('ascii')
            print("RECEIVEED >",x)
            if x == "bye" or x == "Bye" or x == "BYE":
                self.closeNow = True
                self.closeSocket()
                return
    
    """send function takes input from user from console and sends it through tcp socket connection"""            
    def send(self):
        while True:
            msg = input()
            if self.closeNow == False:
                msgToSend = bytearray()
                li = [ord(c) for c in msg]
                for c in li:
                    msgToSend.append(c)
                self.s.send(msgToSend)
                print("SENT >",msgToSend.decode())
            else:
                print("couldn't send the message as Connection Closed...")
                return
    
    """startThreads starts 2 threads one for receiving and one for sending"""        
    def startThreads(self):
        threads = []
        t1 = threading.Thread(target=self.send)
        threads.append(t1)
        t2 = threading.Thread(target=self.receive)
        threads.append(t2)
        t1.start()
        t2.start()
        
    """closes the socket"""   
    def closeSocket(self):
        self.s.close()
        
#creating object of the class leading to connecting to specified socket address
socket = clientTCP("xxx.xxx.xxx.xxx",0000)

