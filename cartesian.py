from astropy.coordinates import Angle
import numpy as np


def dms_to_rad(dms_str):
    d, m, s = map(float, dms_str.split())
    degrees = d + m/60 + s/3600
    radians = np.radians(degrees)
    return radians


def hms_to_rad(hms_str):
    h, m, s = map(float, hms_str.split())
    degrees = 15 * (h + m/60 + s/3600)
    radians = np.radians(degrees)
    return radians


def polar2cartesian(ra, dec, distance):
    ra = Angle(ra, unit='hourangle')
    dec = Angle(dec, unit='deg')
    ra_rad = ra.radian
    dec_rad = dec.radian
    print(type(ra_rad), type(dec_rad))
    x = distance * np.cos(dec_rad) * np.cos(ra_rad)
    y = distance * np.cos(dec_rad) * np.sin(ra_rad)
    z = distance * np.sin(dec_rad)
    return x, y, z
