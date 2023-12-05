import random


def get_random_rgb() -> str:
    return f'{random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)}'
