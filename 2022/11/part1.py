from operator import itemgetter
from math import prod


def read_monkeys(filename):
    with open(filename) as f:
        monkey_notes = f.read().split("\n\n")

    monkeys = {}
    for i, m in enumerate(monkey_notes):
        notes = m.split("\n")
        monkeys[i] = {
            "items": [int(j) for j in notes[1].split(": ")[1].split(", ")],
            "operation": notes[2].split("= ")[1],
            "mod": int(notes[3].split(" ")[-1]),
            "True": int(notes[4].split(" ")[-1]),
            "False": int(notes[5].split(" ")[-1]),
            "inspected": 0,
        }

    return monkeys


def take_turn(monkeys, i):
    for old in monkeys[i]["items"]:
        new = int(eval(monkeys[i]["operation"]) / 3)
        throw_to = monkeys[i][str(not bool(new % monkeys[i]["mod"]))]
        monkeys[throw_to]["items"].append(new)
        monkeys[i]["inspected"] += 1
    monkeys[i]["items"] = []
    return monkeys


if __name__ == "__main__":
    monkeys = read_monkeys("monkeys.txt")
    for n in range(20):
        for i in range(len(monkeys)):
            take_turn(monkeys, i)
    top_two = sorted(monkeys.values(), key=itemgetter("inspected"), reverse=True)[:2]
    monkey_biz = prod(i["inspected"] for i in top_two)
    print("level of monkey business:", monkey_biz)
