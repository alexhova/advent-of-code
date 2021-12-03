from part1 import read_diagnostics, calculate_rates


def mode(readings, i):
    length = len(readings)
    total = sum([int(r[i]) for r in readings])
    if total >= length / 2:
        return "1"
    else:
        return "0"


totals, count, lines, length = read_diagnostics()
gamma, epsilon = calculate_rates(totals, count)

oxys = [line.strip() for line in lines if line.startswith(gamma[0])]
co2s = [line.strip() for line in lines if line.startswith(epsilon[0])]
i = 1
while i < length or not (len(oxys) == len(co2s) == 1):
    oxys = [oxy for oxy in oxys if oxy[i] == mode(oxys, i)] if len(oxys) > 1 else oxys
    co2s = [co2 for co2 in co2s if co2[i] != mode(co2s, i)] if len(co2s) > 1 else co2s
    i += 1

life_support = int(oxys.pop(), 2) * int(co2s.pop(), 2)
print(f"life support rating is {life_support}")
