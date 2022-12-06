def read_signal() -> str:
    with open("signal.txt") as f:
        return f.read().strip()


def unique(chars: str) -> bool:
    for char in chars:
        if chars.count(char) > 1:
            return False
    return True


if __name__ == "__main__":
    signal = read_signal()
    for i in range(0, len(signal)):
        if unique(signal[i : i + 4]):
            print(f"first marker after character {i+4}")
            break
