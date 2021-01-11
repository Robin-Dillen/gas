from verdeling.Clock import clock
from verdeling.Parser import parse
import datetime
from time import sleep
from verdeling.Reservatiesysteem_Contracts import Reservatiesysteem

# vertaling van parser naar functie
cmds = {
    'zaal': 'addZaal',
    'film': 'addFilm',
    'vertoning': 'addVertoning',
    'gebruiker': 'maakAccount',
    'reserveer': 'addReservatie',
    'ticket': 'updateTicketten',
}


class Execute:
    def __init__(self, filename: str):
        self.parsed = parse(filename)  # parsed de filename
        self.run()  # runt de parsed file

    def run(self):
        for line in self.parsed:
            if 'time' in line:  # wacht als er op een tijdstip gewacht moet worden
                self.await_(line['time'])
                if line['cmd'] == 'reserveer':
                    line['args'].insert(0, line['time'])

            clock.toggle()  # schakelt de clock uit

            if len(line['args']) == 0:
                eval('self.' + line['cmd'] + '()')
                continue

            print(cmds[line['cmd']] + str(tuple(line['args'])))
            eval('self.r.' + cmds[line['cmd']] + str(tuple(line['args'])))  # self.r.func(args)

            clock.toggle()  # zet de clock terug aan

    def init(self):
        print('init')
        self.r = Reservatiesysteem()

    def start(self):
        # setup the clock
        dt = datetime.datetime(2020, 10, 5)
        dt = dt.replace(hour=8, minute=0, second=0, microsecond=0)
        clock.setTime(dt)
        clock.start()

    def log(self):
        print("log")
        self.r.makeLog(str(clock))
        # exit()

    def await_(self, time: datetime.datetime):
        clock.setTime(time)  # sets clock time to desired time


e = Execute('system.txt')
