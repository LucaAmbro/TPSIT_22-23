def inizio_fine(func):
    def wrapper():
        print("Inizio")
        func()
        print("Fine")
    return wrapper
@inizio_fine
def ciao():
    print("Ciao")
#ciao = inizio_fine(ciao)
@inizio_fine
def hello():
    print("Hello")
#hello = inizio_fine(hello)

if __name__ == "__main__":
    ciao()
    hello()