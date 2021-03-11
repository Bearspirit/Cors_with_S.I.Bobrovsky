import random
import string

def string_gen(N):
    gen_string = "".join(random.choice(string.digits) for i in range(N))
    return gen_string

