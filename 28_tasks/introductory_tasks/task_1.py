"""
Белка колет орешки и находит алмазы, количество алмазов равно первой цифре факториала
количества орешков, которые расколола белка
"""

def squirrel(N):
    factorial_for_nuts_number = 1
    is_positive = N >= 0
    is_integer = isinstance(N,int)
    if is_integer and is_positive:
        for i in range(1, N+1):
            factorial_for_nuts_number = i*factorial_for_nuts_number
        diamonds_amount = str(factorial_for_nuts_number)
        return int(diamonds_amount[0])
    else:
        return False
