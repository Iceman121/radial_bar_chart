# ==============================================================================
# Importing Modules
# ==============================================================================
import numpy as np
from ..data import user_input

# ==============================================================================
# Figure Parameters
# ==============================================================================
# Total size of graph
width = 800
height = 800

# Data to be used in the graph
gram_colors = {}
drug_colors = {}
df = user_input.import_data()

# Colors
theme = int(input("Dark(1)/Light(0) theme? : "))
if theme == 0:
    bckcol = "#f0e1d2"
    lincol = '#ffffff'
    gram_colors['positive'] = "#aeaeb8"
    gram_colors['negative'] = "#e69584"
    drug_colors['Penicillin'] = '#0d3362'
    drug_colors['Streptomycin'] = '#c64737'
    drug_colors['Neomycin'] = '#000000'
    textcol = '#000000'

elif theme == 1:
    bckcol = "#000000"
    lincol = '#657a84'
    gram_colors['positive'] = "#a92f41"
    gram_colors['negative'] = "#b48375"
    drug_colors['Penicillin'] = '#e5d5c5'
    drug_colors['Streptomycin'] = '#91c7a9'
    drug_colors['Neomycin'] = '#3f3f3f'
    textcol = '#ffffff'

else:
    print("Invalid entry, selecting dark theme...")
    bckcol = "#49626e"
    lincol = '#657a84'
    gram_colors['positive'] = "#81894d"
    gram_colors['negative'] = "#846889"
    drug_colors['Penicillin'] = '#a28fa6'
    drug_colors['Streptomycin'] = '#f2f6d4'
    drug_colors['Neomycin'] = '#ffffff'
    textcol = '#fcecd9'

# ==============================================================================
# Defining Radii
# ==============================================================================
# Radius of the graph
inner_radius = 90
outer_radius = 300 - 10

# Display units on graph
minr = np.sqrt(np.log(.001 * 1E4))
maxr = np.sqrt(np.log(1000 * 1E4))

# Mapping Display Units
unitr = (outer_radius - inner_radius) / (minr - maxr)
baseliner = inner_radius - unitr * maxr


# Calculate Radius of annular rings
def rad(mic):
    return unitr * np.sqrt(np.log(mic * 1E4)) + baseliner

# ==============================================================================
# Angular Parameters
# ==============================================================================
# Angular placement of each bar and section
big_angle = 2.0 * np.pi / (len(df) + 1)
small_angle = big_angle / 7
