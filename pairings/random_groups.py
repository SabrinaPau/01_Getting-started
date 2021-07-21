import random

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

n = ['lea', 'christina', 'benedikt','christian', 'theresa', 'dominic', 'christoph', 'lily', 'till', 'fabian', 'wolfgang']

random.shuffle(n)

print(list(chunks(n, 2)))