# basic bokeh line graph plotting
from bokeh.plotting import figure
from bokeh.io import output_file, show

# prepare data
x = [1, 3, 5, 6]
y = [2, 6, 7, 5]  # these two list should have the same amt of data

# prepare a output file
output_file("Line.html")

# prepare figure
f = figure()

# start plotting
f.line(x, y)  # instead of line, circle and triangle can also be used

show(f)
