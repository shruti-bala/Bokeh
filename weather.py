from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

df = pandas.read_excel("verlegenhuken.xlsx")
x = df["Temperature"]
y = df["Pressure"]

output_file("Weather.html")
f = figure(width = 1000, tools = "pan")
f.title.text = "Temperature and Pressure"
f.title.text_color = "Grey"
f.xaxis.axis_label = "Temperature(°C)"
f.yaxis.axis_label = "Pressure(hPa)"

f.circle(x/10,y/10, size = 0.5)

show(f)