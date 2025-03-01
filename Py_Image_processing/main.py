from re import I
import numpy as py
import imageio as io
import cmath as cm


def fr_func(x:float,y:float,u:int,v:int) -> float:
    # (u,v) are the indices of the MAT[n,n]
    # (x,y) are the absolute indices of the current pixel in the transformed image
    # term1 is the transform coefficent
    term1 = -1j*2*cm.pi*((u*x+v*y)/2)
    py.exp(term1)
    return 0.0


def dft(x:float,y:float) -> float:
    return 0.0



term1 = 1j
print(term1)
