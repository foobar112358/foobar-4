#!/usr/bin/env python

# TLE
def answer(M, F):
    M, F = int(M), int(F)
    gen = 0
    possible = False
    while M > 0 and F > 0:
        if M == 1 and F == 1:
            possible = True
            break
        if M < F:
            M, F = F, M

        M = M - F
        gen += 1

    if not possible:
        return 'impossible'
    else:
        return str(gen)

M = '3'
F = '100000'
print answer(M, F)
