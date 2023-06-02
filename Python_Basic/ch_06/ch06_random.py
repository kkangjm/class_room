import random

def lotto(n, max):
    selected = []

    for i in range(n):
        num = random.randint(1, max)

        while num in selected:
            num = random.randint(1, max)

        selected.append(num)

    return selected

print(lotto(8,100))
