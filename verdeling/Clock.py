import threading
import time
import datetime


class _Clock:
    def __init__(self):
        self.clock = datetime.datetime.now()
        self.p = threading.Thread(target=self.__start, daemon=True)
        self.pause = False
        self.initialized = False
        self.wait = 0.5  # wait time in seconds
        self.increment = 5  # increment amount in minutes

    def start(self):
        """
        start de clock
        :return: None
        """
        self.initialized = True
        self.p.start()

    def __start(self):
        """
        telt elke 0.5 seconden 5 minuten bij de clock
        :return:
        """
        t = time.time()
        while True:
            if not self.pause:
                if time.time() - t > self.wait:
                    print(end='\r')
                    t = time.time()
                    self.clock += datetime.timedelta(minutes=self.increment)
                    print(self, end="\t")

    def toggle(self):
        self.pause = not self.pause

    def getTime(self):
        return self.clock

    def setTime(self, time: datetime.datetime):
        self.clock = time

    def isInitialized(self):
        return self.initialized

    def setWait(self, amount):
        self.wait = amount

    def setIncrement(self, amount):
        self.increment = amount

    def __str__(self):
        return str(self.clock)

clock = _Clock()