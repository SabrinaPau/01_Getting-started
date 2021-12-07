import random

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

n = ['Tobias', 'Jakob', 'Dexter', 'Philipp', 'Pascal', 'Evans', 'Alexander', 'Andrè', 'Jan', 'Patrick', 'Jayaprakash', 'Carolin', 'Victor', 
     'Andreas', 'Zuzanna', 'Maximilian']

random.shuffle(n)

print(list(chunks(n, 2)))
