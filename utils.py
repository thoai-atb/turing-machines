'''Lerp between angles in degree'''
def lerp_angle(a, b, t):
    a %= 360
    b %= 360
    target = b
    if a > b:
        if a - b > 180:
            a -= 360
    else:
        if b - a > 180:
            target = b - 360
    return (1 - t) * a + t * target
