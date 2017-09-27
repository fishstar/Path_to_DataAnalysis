from bokeh.models import Button
from bokeh.plotting import figure, ColumnDataSource
from bokeh.layouts import column, widgetbox
from bokeh.io import curdoc
import numpy as np

N = 200
x = np.linspace(0, 10, N)
y = np.sin(x) + np.random.random(N)
source = ColumnDataSource(data={'x':x, 'y':y})

plot = figure()
plot.circle('x', 'y', source=source)

# Create a Button with label 'Update Data'
button = Button(label='Update Data')

# Define an update callback with no arguments: update
def update():

    # Compute new y values: y
    y = np.sin(x) + np.random.random(N)

    # Update the ColumnDataSource data dictionary
    source.data = {'x':x, 'y':y}

# Add the update callback to the button
button.on_click(update)

# Create layout and add to current document
layout = column(widgetbox(button), plot)
curdoc().add_root(layout)