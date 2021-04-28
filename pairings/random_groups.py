import random

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

n = ['constantin', 'dirk', 'gero', 'jenny', 'manuel', 'martin', 'pascal', 'paul']

random.shuffle(n)

print(list(chunks(n, 2)))