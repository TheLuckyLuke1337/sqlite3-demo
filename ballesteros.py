def ballesteros(b, v):
    bv = b-v
    return 4600 * (1/(0.92 * bv + 1.7) + 1/(0.92 * bv + 0.62))
