from typing import List
import re
import datetime


def parse(filename: str) -> list:
    """
    parsed de files in een handiger formaat om uit te voeren
    """
    deleted = delete_comments(filename)  # leest de file in, splitst de lijnen in een lijst en verwijdert de comments
    splitted = [dict]*len(deleted)  # maakt een lege lijst van dicts
    for i, line in enumerate(deleted):  # itereert over de lijnen
        line = line.split(' ')  # splitst de lijnen
        if re.fullmatch(r"^(\d\d\d\d-\d\d-\d\d)", line[0]):  # checkt of het eerste element een datum is
            merged_time = datetime.datetime.fromisoformat(line[0] + ' ' + line[1])  # zet de datum om naar een datetime object
            newline = {'cmd': line[2], 'args': line[3:], 'time': merged_time}  # maakt een nieuw commando aan
        else:
            newline = {'cmd': line[0], 'args': line[1:]}  # maakt een nieuw commando aan

        splitted[i] = newline

    open = 0
    close = 0
    slots = {1: datetime.time(14, 30), 2: datetime.time(17, 0), 3: datetime.time(20, 0), 4: datetime.time(22, 30)}
    for line in splitted:  # itereert over de commandos
        pop = -1
        for i, arg in enumerate(line['args']):  # itereert over de argumenten van het commando
            if arg == '':  # als het argument leeg is, verwijder het argument
                line['args'].pop(i)
                continue

            if re.match(r"^(\d\d\d\d-\d\d-\d\d)", arg):  # als argument datum is, convert naar datetime object
                line['args'][i] = datetime.datetime.fromisoformat(arg)
                continue

            if arg[0] == '"':
                open = i
                continue

            if arg[-1] == '"':
                close = i
                continue

            if re.match(r"\d", arg):  # checkt of er een digit in het argument zit
                if i == 2 and line['cmd'] == "vertoning":
                    line['args'][i] = slots[int(arg)]
                    continue
                arg = float(arg)
                if arg == int(arg):
                    line['args'][i] = int(arg)
                    continue
                line['args'][i] = float(arg)
                continue

        if open != close:  # als dubbele quotes niet correct gesloten zijn, merge de argumenten
            line['args'][open] += " " + line['args'][close]
            line['args'].pop(close)
            line['args'][open] = line['args'][open][1:-1]
            open = 0
            close = 0

        if pop != -1:
            line['args'].pop(pop)

    return splitted


def delete_comments(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        f = f.read()
        lines = f.split("\n")
        for i in range(len(lines) - 1, -1, -1):
            if lines[i] == '' or lines[i][0] == '#':
                lines.pop(i)

    return lines


