from socket import AF_INET, SO_BROADCAST, SOCK_STREAM, socket

def chatClient(ip, port):
    with socket (AF_INET, SOCK_STREAM) as s:
        s.connect((ip, port))
        s.send("avanti".encode('utf-8'))

if __name__ == "__main__":
    ip = input("Inserisci ip: ")
    port = int(input("Inserisci porta: "))
    chatClient(ip, port)