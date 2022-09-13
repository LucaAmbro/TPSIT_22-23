from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 1024

IP = "192.168.95.255"
PORT = 5000
# possibilità
# localhost 127.0.0.1

def chatClient():
    running = True
    with socket(AF_INET, SOCK_DGRAM) as s:
        while running == True:
            mex = input("Inserire il messaggio: ")
            if mex == 'esci' or mex == 'ESCI':
                running = False
            else:
                mex = mex.encode()
                s.sendto(mex, (IP, PORT))

if __name__ == "__main__":
    chatClient()