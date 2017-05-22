import os
import numpy as np
path = os.getcwd()
from ..data import user_input

width = 800
height = 800
inner_radius = 90
outer_radius = 300 - 10

minr = np.sqrt(np.log(.001 * 1E4))
maxr = np.sqrt(np.log(1000 * 1E4))
unitr = (outer_radius - inner_radius) / (minr - maxr)
baseliner = inner_radius - unitr * maxr

gram_colors = user_input.import_gram_colors()
drug_colors = user_input.import_drug_colors()
df = user_input.import_data()

big_angle = 2.0 * np.pi / (len(df) + 1)
small_angle = big_angle / 7


def rad(mic):
    return unitr * np.sqrt(np.log(mic * 1E4)) + baseliner
