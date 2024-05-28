from threading import Lock, Condition

class FizzBuzz:
    def __init__(self, n):
        self.n = n
        self.current = 1
        self.lock = Lock()
        self.cv = Condition(self.lock)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz):
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 3 != 0 or self.current % 5 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    return
                printFizz()
                self.current += 1
                self.cv.notify_all()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz):
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 5 != 0 or self.current % 3 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    return
                printBuzz()
                self.current += 1
                self.cv.notify_all()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz):
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 15 != 0):
                    self.cv.wait()
                if self.current > self.n:
                    return
                printFizzBuzz()
                self.current += 1
                self.cv.notify_all()

    # printNumber(x) outputs "x", where x is an integer
    def number(self, printNumber):
        while True:
            with self.cv:
                while self.current <= self.n and (self.current % 3 == 0 or self.current % 5 == 0):
                    self.cv.wait()
                if self.current > self.n:
                    return
                printNumber(self.current)
                self.current += 1
                self.cv.notify_all()
import threading

def printFizz():
    print("fizz", end=' ')

def printBuzz():
    print("buzz", end=' ')

def printFizzBuzz():
    print("fizzbuzz", end=' ')

def printNumber(number):
    print(number, end=' ')

n = 15
fizzbuzz = FizzBuzz(n)

threads = [
    threading.Thread(target=fizzbuzz.fizz, args=(printFizz,)),
    threading.Thread(target=fizzbuzz.buzz, args=(printBuzz,)),
    threading.Thread(target=fizzbuzz.fizzbuzz, args=(printFizzBuzz,)),
    threading.Thread(target=fizzbuzz.number, args=(printNumber,))
]

for t in threads:
    t.start()

for t in threads:
    t.join()
