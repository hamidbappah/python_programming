# generator: lazy values, tiny memory
def read_scores(path):
    with open(path) as f:
        for line in f:
            yield int(line)

total = sum(read_scores('big.txt'))
