import Cinema
from Cinema import clock
from Parser import parse
import datetime
from time import sleep

cmds = {
    'zaal': 'add_zaal',
    'film': 'add_movie',
    'vertoning': 'add_vertoning',
    'gebruiker': 'create_account',
    'reserveer': 'place_reservation',
    'ticket': 'update_vertoning',
}


class Execute:
    def __init__(self, filename: str):
        self.parsed = parse(filename)
        self.run()

    def run(self):
        for line in self.parsed:
            if 'time' in line:
                self.await_(line['time'])
                if line['cmd'] == 'reserveer':
                    line['args'].insert(0, line['time'])

            clock.toggle()

            if len(line['args']) == 0:
                eval('self.' + line['cmd'] + '()')
                continue

            print(cmds[line['cmd']] + str(tuple(line['args'])))
            eval('self.r.' + cmds[line['cmd']] + str(tuple(line['args'])))

            clock.toggle()

    def init(self):
        print('init')
        self.r = Cinema.ReservatieSysteem()

    def start(self):
        dt = datetime.datetime(2020, 10, 5)
        dt = dt.replace(hour=8, minute=0, second=0, microsecond=0)
        clock.setTime(dt)
        clock.start()

    def log(self):
        self.r.log(str(clock))
        exit()

    def await_(self, time):
        while clock.getTime() < time:
            pass


e = Execute('system.txt')
