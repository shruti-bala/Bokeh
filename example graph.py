from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df = pandas.read_csv("bachelors.csv")
x = df["Year"]
y = df["Engineering"]

output_file("bachelor.html")
f = figure(plot_width = 1000, plot_height = 400)
f.title.text = "Bachelors"
f.xaxis.minor_tick_line_color = 252, 40, 3
f.xaxis.axis_label = "Year"
f.yaxis.axis_label = "No. of Bachelors"

f.line(x,y)

show(f)
