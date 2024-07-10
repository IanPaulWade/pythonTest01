""" Test script for metocean derivative module """
# Ian P Wade (May 2022)

import metoc_derivatives as md

# %%
# the following requires a restart of Spyder kernal in IPython Console
# following any change of default environment via preferences

# from platform import python_version
# print(f"Python version: {python_version()}")

# %%
# data input
H = 5.65
T = 10.4

# derive wave steepness (individual or seastate)
S = md.steepness_from_ht(H, T)
print('Significant Steepness = ' + f"{S:0.1f}")

# calculate T from H and S (individual or seastate)
newT = md.period_from_hs(H, S)
print('Original Tz = ' + f"{T:0.1f}" + ' s : New Tz = ' + f"{newT:0.1f}" + ' s')

# calculate H from T and S (individual or seastate)
newH = md.height_from_ts(T, S)
print('Original Hs = ' + f"{H:0.2f}" + ' m : New Hs = ' + f"{newH:0.1f}" + ' m')

# %%
# data input
spd_mps = 40

# convert m/s to knots
spd_kts = md.mps_to_knots(spd_mps)

# and back to m/s
new_spd_mps = md.knots_to_mps(spd_kts)

print('Original m/s = ' f"{spd_mps:0.2f}" + ' m/s :')
print('Derived knots = ' f"{spd_kts:0.2f}" + ' kts :')
print('Recalculated m/s = ' f"{new_spd_mps:0.2f}" + ' m/s :')

# %%
# data input
U = 1.0
V = 1.0
DIR_CONV = 'V'

# convert u, v to magnitude and direction (2 dir conventions available)
mg, dr = md.uv_to_md(U, V, DIR_CONV)
print('U = ' f"{U:0.2f}" + ' m/s :')
print('V = ' f"{V:0.2f}" + ' m/s :')
print('Mag = ' f"{mg:0.2f}" + ' m/s :')
print('Dir = ' f"{dr:0.1f}" + ' degT :')
