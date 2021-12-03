def read_diagnostics():
    with open("diagnostics.txt") as f:
        lines = f.readlines()
    length = len(lines[0].strip())
    totals = [0] * length
    count = len(lines)
    for line in lines:
        totals = [totals[i] + int(line[i].strip()) for i in range(length)]
    return totals, count, lines, length


def calculate_rates(totals, count):
    gamma = ""
    epsilon = ""
    for ones in totals:
        zeroes = count - ones
        if ones > zeroes:
            gamma += "1"
            epsilon += "0"
        elif zeroes > ones:
            gamma += "0"
            epsilon += "1"
    return gamma, epsilon


def power_consumption(gamma, epsilon):
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    totals, count, _, _ = read_diagnostics()
    gamma, epsilon = calculate_rates(totals, count)
    power = power_consumption(gamma, epsilon)
    print(f"power consumption is {power}")
