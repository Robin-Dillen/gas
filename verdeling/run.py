import threading
import time
import datetime


class _Clock:
    def __init__(self):
        self.clock = datetime.datetime.now()
        self.p = threading.Thread(target=self.__start, daemon=True)
        self.pause = False

    def start(self):
        self.p.start()

    def __start(self):
        t = time.time()
        while True:
            if not self.pause:
                if time.time() - t > 0.01:
                    print(end='\r')
                    t = time.time()
                    self.clock += datetime.timedelta(minutes=5)
                    print(self, end="")

    def toggle(self):
        self.pause = not self.pause

    def getTime(self):
        return self.clock

    def setTime(self, time: datetime.datetime):
        self.clock = time

    def __str__(self):
        return str(self.clock)


clock = _Clock()