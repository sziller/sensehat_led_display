import random as rnd


def mode_0(**kwargs):
    coldict = kwargs['coldict']
    return [coldict[rnd.randint(0, 9)] for _ in range(64)]


def mode_1(**kwargs):
    coldict = kwargs['coldict']
    return [coldict[rnd.randint(5, 9)]] * 64

def mode_2(**kwargs):
    coldict = kwargs['coldict']
    ellapsed = kwargs['ellapsed']
    speed = 4
    base_matrix = [coldict[0] for _ in range(64)]
    actual_matrix = [coldict[0] for _ in range(64)]
    actual_matrix[((int(ellapsed * speed)) + 0) % 64] = (255, 255, 255)
    # actual_matrix[((int(ellapsed * speed)) + 1) % 64] = (255, 255, 255)
    return actual_matrix

def mode_3(**kwargs):
    coldict = kwargs['coldict']
    ellapsed = kwargs['ellapsed']
