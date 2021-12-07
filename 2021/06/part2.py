fish = {}
for k in range(9):
    fish[k] = 0

with open("lanternfish.txt") as f:
    for n in f.read().strip().split(","):
        fish[int(n)] += 1

for _ in range(256):
    babies = fish[0]
    for k in range(8):
        fish[k] = fish[k + 1]
    fish[8] = babies
    fish[6] += babies

print(f"lanternfish population after 256 days: {sum(fish.values())}")
