from socket import AF_INET, SO_BROADCAST, SOCK_DGRAM, socket
from ssl import SOL_SOCKET

#BUFFER_SIZE = 1024
BUFFER_SIZE = 131072

mystr = "ciao" # str
# bytes

HOST = "0.0.0.0"
PORT = 5000
# possibilità
# localhost 127.0.0.1

def chatServer(host, port):
    running = True
    with socket (AF_INET, SOCK_DGRAM) as s:
        s.bind((host, port))
        # s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) LINUX E MACOS
        img = []
        pdf = b''
        print('In ascolto')
        while running == True:
            msg = s.recvfrom(BUFFER_SIZE)
            if len(msg[0]) == 4096:
                #img = img.append(msg[0])
                pdf = pdf + msg[0]
            else:
                running = False
        #img = img.append(msg[0])
        pdf = pdf + msg[0]
        f = open("stampa.pdf", "wb")
        #print(img)
        #f.write(b''.join(img))
        f.write(pdf)
        #print(msg)

if __name__ == "__main__":
    chatServer(HOST, PORT)