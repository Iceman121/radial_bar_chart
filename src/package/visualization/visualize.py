# ==============================================================================
# Importing Modules
# ==============================================================================
from bokeh.plotting import figure, show
from ..global_variables import global_var
import numpy as np

# ==============================================================================
# Importing Global Variables
# ==============================================================================
width = global_var.width
height = global_var.width
df = global_var.df
big_angle = global_var.big_angle
small_angle = global_var.small_angle
gram_color = global_var.gram_colors
drug_color = global_var.drug_colors
inner_radius = global_var.inner_radius
outer_radius = global_var.outer_radius
bckcol = global_var.bckcol
lincol = global_var.lincol


# Function for call
def plot_radial_chart():
    # Figure level arguments
    p = figure(plot_width=width, plot_height=height, title="",
               x_axis_type=None, y_axis_type=None,
               x_range=(-420, 420), y_range=(-420, 420),
               min_border=0, outline_line_color="black",
               background_fill_color=bckcol, border_fill_color=bckcol,
               toolbar_sticky=False)

    # Grid Line Colors
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None

    # Classifier Wedges
    angles = np.pi/2 - big_angle/2 - df.index.to_series()*big_angle
    colors = [gram_color[gram] for gram in df.gram]
    p.annular_wedge(0, 0,
                    inner_radius,
                    outer_radius,
                    -big_angle+angles,
                    angles,
                    color=colors,)

    # Individual Bars
    p.annular_wedge(0, 0, inner_radius, global_var.rad(df.penicillin),
                    -big_angle+angles+5*small_angle,
                    -big_angle+angles+6*small_angle,
                    color=drug_color['Penicillin'])
    p.annular_wedge(0, 0, inner_radius, global_var.rad(df.streptomycin),
                    -big_angle+angles+3*small_angle,
                    -big_angle+angles+4*small_angle,
                    color=drug_color['Streptomycin'])
    p.annular_wedge(0, 0, inner_radius, global_var.rad(df.neomycin),
                    -big_angle+angles+1*small_angle,
                    -big_angle+angles+2*small_angle,
                    color=drug_color['Neomycin'])

    # Circular Axes and Lables
    labels = np.power(10.0, np.arange(-3, 4))
    radii = global_var.rad(labels)
    p.circle(0, 0, radius=radii, fill_color=None, line_color=lincol)
    p.text(0, radii[:-1], [str(r) for r in labels[:-1]],
           text_font_size="8pt", text_align="center", text_baseline="middle")

    # Radial Axes
    p.annular_wedge(0, 0, inner_radius-10, outer_radius+10,
                    -big_angle+angles, -big_angle+angles, color="black")

    # Bacteria Labels
    xr = radii[0]*np.cos(np.array(-big_angle/2 + angles))
    yr = radii[0]*np.sin(np.array(-big_angle/2 + angles))
    label_angle = np.array(-big_angle/2+angles)
    # Easier to read labels on the left side
    label_angle[label_angle < -np.pi/2] += np.pi
    p.text(xr, yr, df.bacteria, angle=label_angle,
           text_font_size="9pt", text_align="center", text_baseline="middle")

    # OK, these hand drawn legends are pretty clunky,
    # will be improved in future release
    p.circle([-40, -40], [-370, -390],
             color=list(gram_color.values()), radius=5)
    p.text([-30, -30], [-370, -390],
           text=["Gram-" + gr for gr in gram_color.keys()],
           text_font_size="7pt", text_align="left", text_baseline="middle")

    p.rect([-40, -40, -40], [18, 0, -18], width=30, height=13,
           color=list(drug_color.values()))
    p.text([-15, -15, -15], [18, 0, -18], text=list(drug_color),
           text_font_size="9pt", text_align="left", text_baseline="middle")

    show(p)
