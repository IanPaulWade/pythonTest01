""" Module providing various metocean derivatives """
# Ian P Wade (Jul 2024)

import math

# constants
g = 9.81
pi = 3.142


# WAVES ######################################################################
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


# UNIT CONVERSIONS ###########################################################
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


# VECTOR CONVERSIONS #########################################################
# convert u / v to magnitude / direction
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
        dr = ((180/pi) * math.atan2(-u, -v)) % 360
    elif dir_conv == 'V':
        dr = ((180/pi) * math.atan2(u, v)) % 360
    else:
        dr = -999
        print("Enter 'M' (for Magnitude) or 'V' (for Vector)")

    return mg, dr
