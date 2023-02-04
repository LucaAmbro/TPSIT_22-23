import threading
import time

NUMERO_SIMULAZIONI = 1000
n = 0
NUMERO_SOMME = 10000

def simulation(i):
    global n

    for _ in range(NUMERO_SOMME):
        n = n + 1
    print(str(threading.current_thread().name) + ': ' + str(i) + ', n = ' + str(n))
    

if __name__ == '__main__':
    threads = [threading.Thread(target=simulation, args=(i,)) for i in range(NUMERO_SIMULAZIONI)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()