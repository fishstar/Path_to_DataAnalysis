from bokeh.plotting import figure, ColumnDataSource
from bokeh.layouts import column, widgetbox
from bokeh.io import curdoc
from bokeh.models import Slider
import numpy as np


# Create ColumnDataSource: source
x = np.linspace(0.3, 10, 200)
y = np.sin(1/x)
source = ColumnDataSource(data={'x':x, 'y':y})

# Add a line to the plot
plot = figure()
plot.line('x', 'y', source=source)

# Add a slider
slider = Slider(title='scale', start=1, end=10, step=1, value=1)




# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(scale/x)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider.on_change('value', callback)

# Create layout and add to current document
layout = column(widgetbox(slider), plot)


# Add the layout to the current document
curdoc().add_root(layout)