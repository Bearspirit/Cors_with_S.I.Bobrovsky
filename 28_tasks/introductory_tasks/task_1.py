"""
Белка колит орешки и находит алмазы, количество алмазов равно первой цифре факториала
количества орешков, которые расколола белка
"""

def squirrel(N):
    fac = 1
    if N%1==0 and N >= 0:
        for i in range(1, N+1):
            fac = i*fac
        out = str(fac)
        return int(out[0])
    else:
        return False
