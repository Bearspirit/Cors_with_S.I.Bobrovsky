"""
Белка колит орешки и находит алмазы, количество алмазов равно первой цифре факториала
количества орешков, которые расколола белка
"""

def squirrel(N):
    factorial_for_nuts_number = 1
    if N%1==0 and N >= 0:
        for i in range(1, N+1):
            factorial_for_nuts_number = i*factorial_for_nuts_number
        diamonds_amount = str(factorial_for_nuts_number)
        return int(diamonds_amount[0])
    else:
        return False
