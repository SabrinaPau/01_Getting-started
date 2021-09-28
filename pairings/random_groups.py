import random

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

n = ['Meron', 'Axel', 'Tim', 'Marc', 'Louis', 'Natalie', 'Lea', 'Daniel', 'Sergej', 'Max', 'Arne', 'Christopher', 'Paul']

random.shuffle(n)

print(list(chunks(n, 2)))
