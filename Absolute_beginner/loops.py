# for: known collection
for n in range(1, 6):
    print(n, "squared is", n * n)

# while: unknown repetitions
balance = 1000
years = 0
while balance < 2000:
    balance *= 1.10   # 10% growth
    years += 1
print(f"Doubles in {years} years")
