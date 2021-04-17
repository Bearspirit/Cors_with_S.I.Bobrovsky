import random

for i in range(1, 11):
    name = str(i) + ".txt"
    with open(name, "wt") as nf:
        for k in range(3):
            nf.write(str(random.randint(1, 10)) + "\n")