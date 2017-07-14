import threading

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print threading.currentThread().getName()

x = BuckysMessenger(name='Send out msg')
y = BuckysMessenger(name='Rx msg')
x.start()
y.start()
