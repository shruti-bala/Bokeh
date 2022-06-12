from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

# getting data from csv file
df = pandas.read_csv("data.csv")
x = df["x"] # column named "x"
y = df["y"]

# creating an html file
output_file("CSV.html")

# create figure
f = figure()

# make a plot
f.line(x,y)

show(f)