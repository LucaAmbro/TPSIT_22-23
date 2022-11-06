from asyncio.windows_events import NULL
from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 1024

IP = "192.168.136.255"
PORT = 5000
# possibilità
# localhost 127.0.0.1

def chatClient(ip, port):
    running = True
    with socket(AF_INET, SOCK_DGRAM) as s:
        f = open("Pdf_prova.pdf", "rb")
        buffer = f.read()
        #print(buffer)
        n = 0

        data = True

        """while data:
            data = f.read(4096)
            print(data)
            if data:
                s.sendto(data.encode('utf-8'), (ip, port))
        s.sendto(b'', (ip, port))
        f.close()"""
        try:
            while buffer[(n * 4096) + 4095]:
                m = buffer[n * 4096: n * 4096 + 4095]
                s.sendto(m, (ip, port))
                n += 1
        except:
            n += 1
            m = buffer[n * 4096:]
        s.sendto(m, (ip, port))
        f.close()
      

if __name__ == "__main__":
    ip = input("Inserisci ip: ")
    port = int(input("Inserisci porta: "))
    #nome = input("Inserisci nome utente: ")
    chatClient(ip, port)
