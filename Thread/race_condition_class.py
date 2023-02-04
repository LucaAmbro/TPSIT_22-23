import threading
import time

NUMERO_SIMULAZIONI = 1000
NUMERO_SOMME = 10000

class Incrementa(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x

    def incrementa(self):
        self.x = self.x + 1

class ThreadIncrementa(threading.Thread):
    def __init__(self, x):
        threading.Thread.__init__(self)
        self.x = x
    def run(self):
        #simulation(self.x)
        self.x.incrementa()


def simulation(n):
    for _ in range(NUMERO_SOMME):
        n = n + 1
    print(str(threading.current_thread().name) + ', n = ' + str(n))
    

if __name__ == '__main__':
    x = Incrementa(0)
    threads = [ThreadIncrementa(x) for _ in range(NUMERO_SIMULAZIONI)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(x.x)