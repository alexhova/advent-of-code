from part1 import read_signal, unique

if __name__ == "__main__":
    signal = read_signal()
    for i in range(0, len(signal)):
        if unique(signal[i : i + 14]):
            print(f"first marker after character {i+14}")
            break
