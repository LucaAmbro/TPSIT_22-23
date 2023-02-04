#from threading import Thread
import threading
luc = threading.Lock()
import time

def funzione():
    print("Partenza del thread ", threading.current_thread().name)
    print("Elaboro.......", threading.current_thread().name)
    time.sleep(2)
    print("Finito lavoro ", threading.current_thread().name)

def main():
    t = threading.Thread(target = funzione, name="Primo")
    t.start()
    t.join()
    q = threading.Thread(target = funzione, name="Secondo")
    q.start()
    q.join()

    funzione()
    print("Fine chiamata main \n")

if __name__ == "__main__":
    main()