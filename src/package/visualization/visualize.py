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
section_color = global_var.section_colors
wedge_color = global_var.wedge_colors
inner_radius = global_var.inner_radius
outer_radius = global_var.outer_radius
bckcol = global_var.bckcol
lincol = global_var.lincol
textcol = global_var.textcol


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
    # Cheat here for dictionary use. Resolve after dict is automated.
    colors = [section_color[1] if section == 'positive'
              else section_color[2] for section in df.ix[:, -1]]
    p.annular_wedge(0, 0,
                    inner_radius,
                    outer_radius,
                    -big_angle+angles,
                    angles,
                    color=colors,)

    # Individual Bars
    p.annular_wedge(0, 0, inner_radius, global_var.rad(df.ix[:, 1]),
                    -big_angle+angles+5*small_angle,
                    -big_angle+angles+6*small_angle,
                    color=wedge_color[1])
    p.annular_wedge(0, 0, inner_radius, global_var.rad(df.ix[:, 2]),
                    -big_angle+angles+3*small_angle,
                    -big_angle+angles+4*small_angle,
                    color=wedge_color[2])
    p.annular_wedge(0, 0, inner_radius, global_var.rad(df.ix[:, 3]),
                    -big_angle+angles+1*small_angle,
                    -big_angle+angles+2*small_angle,
                    color=wedge_color[3])

    # Circular Axes and Lables
    labels = np.power(10.0, np.arange(-3, 4))
    radii = global_var.rad(labels)
    p.circle(0, 0, radius=radii, fill_color=None, line_color=lincol)
    p.text(0, radii[:-1], [str(r) for r in labels[:-1]],
           text_font_size="8pt", text_align="center", text_baseline="middle",
           text_color=textcol)

    # Radial Axes
    p.annular_wedge(0, 0, inner_radius-10, outer_radius+10,
                    -big_angle+angles, -big_angle+angles, color="black")

    # Bacteria Labels
    xr = radii[0]*np.cos(np.array(-big_angle/2 + angles))
    yr = radii[0]*np.sin(np.array(-big_angle/2 + angles))
    label_angle = np.array(-big_angle/2+angles)
    # Easier to read labels on the left side
    label_angle[label_angle < -np.pi/2] += np.pi
    p.text(xr, yr, df.ix[:, 0], angle=label_angle,
           text_font_size="9pt", text_align="center", text_baseline="middle",
           text_color=textcol)

    # OK, these hand drawn legends are pretty clunky,
    # will be improved in future release
    p.circle([-40, -40], [-370, -390],
             color=list(section_color.values()), radius=5)
    p.text([-30, -30], [-370, -390],
           text=[sec for sec in df.ix[:, -1].unique()],
           text_font_size="7pt", text_align="left", text_baseline="middle",
           text_color=textcol)

    p.rect([-40, -40, -40], [18, 0, -18], width=30, height=13,
           color=list(wedge_color.values()))
    p.text([-15, -15, -15], [18, 0, -18],
           text=[wed for wed in df.columns[range(1, 4)]],
           text_font_size="9pt", text_align="left", text_baseline="middle",
           text_color=textcol)

    show(p)
