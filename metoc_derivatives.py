""" Module providing various metocean derivatives """
# Ian P Wade (Jul 2024)

import math

# constants
g = 9.81
pi = 3.142


# wave steepness, given height and period
def steepness_from_ht(h, t):
    """ derive steepness (individual or seastate) from height and period """
    s = (g * pow(t, 2)) / (2 * pi * h)
    return s


# wave period, given height and steepness
def period_from_hs(h, s):
    """ derive period (individual or seastate) from height and steepness """
    t = math.sqrt((2 * pi * h * s) / g)
    return t


# wave height, given period and steepness
def height_from_ts(t, s):
    """ derive height (individual or seastate) from period and steepness """
    h = ((g * math.pow(t, 2)) / (2 * pi * s))
    return h


# wave length, given period and depth
def wavelength_from_td(t, d):
    L0 = (g * math.pow(t, 2)) / (2 * pi)
    guess = L0
    L = (g * math.pow(t, 2)) / (2 * pi) * math.tanh((2 * pi) * (d / guess))
    diff = abs(L - guess)
    while diff > 0.01:
        diff = abs(L - guess)
        guess = L + (0.5 * diff)
        L = (g * math.pow(t, 2)) / (2 * pi) * math.tanh((2 * pi) * (d / guess))
    return L0, L


# convert speeds (m/s to knots)
def mps_to_knots(spd_mps):
    """ convert speed in m/s to knots """
    spd_knots = spd_mps / 0.5144
    return spd_knots


# convert speeds (knots to m/s)
def knots_to_mps(spd_kts):
    """ convert speed in knots to m/s"""
    spd_mps = spd_kts * 0.5144
    return spd_mps


def uv_to_md(u, v, dir_conv):
    """
    convert U, V vectors to magnitude and direction
    includes directional convention options ... 
    V = vector (towards - consistent with U, V vectors)
    M = Meteorological (from - reversal of U, V vectors)
    """
    dir_conv = dir_conv.upper()

    mg = math.sqrt(math.pow(u, 2) + math.pow(v, 2))

    if dir_conv == 'M':
        dr = ((180 / pi) * math.atan2(-u, -v)) % 360
    elif dir_conv == 'V':
        dr = ((180 / pi) * math.atan2(u, v)) % 360
    else:
        dr = -999
        mg = -999
        print("Enter 'M' (for Magnitude) or 'V' (for Vector)")

    return mg, dr


def md_to_uv(mg, dr, dir_conv):
    """
    convert magnitude and direction to U, V vectors
    includes directional convention options ...
    V = vector (towards - consistent with U, V vectors)
    M = Meteorological (from - reversal of U, V vectors)
    """
    dir_conv = dir_conv.upper()

    if dir_conv == 'M':
        u = abs(mg) * math.sin((pi / 180) * dr)
        v = abs(mg) * math.cos((pi / 180) * dr)
    elif dir_conv == 'V':
        u = abs(mg) * math.sin((pi / 180) * dr)
        v = abs(mg) * math.cos((pi / 180) * dr)
    else:
        u = -999
        v = -999
        print("Enter 'M' (for Magnitude) or 'V' (for Vector)")

    return u, v
