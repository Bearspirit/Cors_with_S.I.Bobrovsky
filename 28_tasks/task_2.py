def odometer(massive):
    if len(massive) >= 2:
        x = massive[0] * massive[1]
        for i in range(2, len(massive), 2):
            x = (massive[i] * (massive[i+1] - massive[i-1])) + x
        return x
    else:
        return False
