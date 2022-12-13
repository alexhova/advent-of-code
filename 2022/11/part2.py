from part1 import read_monkeys
from operator import itemgetter
from math import prod


def take_turn(monkeys, i, big_mod):
    for old in monkeys[i]["items"]:
        new = int(eval(monkeys[i]["operation"])) % big_mod
        throw_to = monkeys[i][str(not bool(new % monkeys[i]["mod"]))]
        monkeys[throw_to]["items"].append(new)
        monkeys[i]["inspected"] += 1
    monkeys[i]["items"] = []
    return monkeys


if __name__ == "__main__":
    monkeys = read_monkeys("monkeys.txt")
    big_mod = prod(monkey["mod"] for monkey in monkeys.values())
    for n in range(10000):
        for i in range(len(monkeys)):
            take_turn(monkeys, i, big_mod)
    top_two = sorted(monkeys.values(), key=itemgetter("inspected"), reverse=True)[:2]
    monkey_biz = prod(i["inspected"] for i in top_two)
    print("level of monkey business:", monkey_biz)
