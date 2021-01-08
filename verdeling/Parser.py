from typing import List
import re
import datetime


def parse(filename: str) -> list:
    deleted = delete_comments(filename)
    splitted = [dict]*len(deleted)
    for i, line in enumerate(deleted):
        line = line.split(' ')
        if re.fullmatch(r"^(\d\d\d\d-\d\d-\d\d)", line[0]):
            merged_time = datetime.datetime.fromisoformat(line[0] + ' ' + line[1])
            newline = {'cmd': line[2], 'args': line[3:], 'time': merged_time}
        else:
            newline = {'cmd': line[0], 'args': line[1:]}

        splitted[i] = newline

    open = 0
    close = 0
    slots = {1: datetime.time(14, 30), 2: datetime.time(17, 0), 3: datetime.time(20, 0), 4: datetime.time(22, 30)}
    for line in splitted:
        pop = -1
        for i, arg in enumerate(line['args']):
            if arg == '':
                line['args'].pop(i)
                continue

            if re.match(r"^(\d\d\d\d-\d\d-\d\d)", arg):
                line['args'][i] = datetime.datetime.fromisoformat(arg)
                continue

            if arg[0] == '"':
                open = i
                continue

            if arg[-1] == '"':
                close = i
                continue

            if re.match(r"\d", arg):
                if i == 2 and line['cmd'] == "vertoning":
                    line['args'][i] = slots[int(arg)]
                    continue
                arg = float(arg)
                if arg == int(arg):
                    line['args'][i] = int(arg)
                    continue
                line['args'][i] = float(arg)
                continue

        if open != close:
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


