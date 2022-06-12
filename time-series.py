from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df = pandas.read_csv("adbe.csv", parse_dates=["Date"])
x = df["Date"]
y = df["Volume"]

output_file("Date.html")
f = figure(x_axis_type = "datetime",width = 1000)

f.line(x,y)
show(f)