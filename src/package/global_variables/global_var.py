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
section_colors = {}
wedge_colors = {}
df = user_input.import_data()

# Colors
theme = int(input("Light(0)/Dark(1) theme? : "))
if theme == 0:
    bckcol = "#f0e1d2"
    lincol = '#ffffff'
    section_colors[1] = "#aeaeb8"
    section_colors[2] = "#e69584"
    wedge_colors[1] = '#0d3362'
    wedge_colors[2] = '#c64737'
    wedge_colors[3] = '#000000'
    textcol = '#000000'

elif theme == 1:
    bckcol = "#000000"
    lincol = '#657a84'
    section_colors[1] = "#a92f41"
    section_colors[2] = "#b48375"
    wedge_colors[1] = '#e5d5c5'
    wedge_colors[2] = '#91c7a9'
    wedge_colors[3] = '#3f3f3f'
    textcol = '#ffffff'

else:
    print("Invalid entry, selecting dark theme...")
    bckcol = "#000000"
    lincol = '#657a84'
    section_colors[1] = "#a92f41"
    section_colors[2] = "#b48375"
    wedge_colors[1] = '#e5d5c5'
    wedge_colors[2] = '#91c7a9'
    wedge_colors[3] = '#3f3f3f'
    textcol = '#ffffff'

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
