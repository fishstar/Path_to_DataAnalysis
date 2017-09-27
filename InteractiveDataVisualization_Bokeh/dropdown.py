import pandas as pd
from bokeh.models import Select
from bokeh.plotting import figure, ColumnDataSource
from bokeh.layouts import row, widgetbox
from bokeh.io import curdoc

# Read data
df = pd.read_csv('literacy_birth_rate.csv')
df = df.rename(columns={'Country ':'Country', 'female literacy':'female_literacy'})
df.female_literacy = pd.to_numeric(df.female_literacy, errors='coerce')
df.fertility = pd.to_numeric(df.fertility, errors='coerce')
df = df.dropna()


# Create ColumnDataSource: source
source = ColumnDataSource(data={
    'x' : df.fertility,
    'y' : df.female_literacy
})

# Create a new plot: plot
plot = figure()

# Add circles to the plot
plot.circle('x', 'y', source=source)

# Define a callback function: update_plot
def update_plot(attr, old, new):
    # If the new Selection is 'female_literacy', update 'y' to female_literacy
    if new == 'female_literacy': 
        source.data = {
            'x' : df.fertility,
            'y' : df.female_literacy
        }
    # Else, update 'y' to population
    else:
        source.data = {
            'x' : df.fertility,
            'y' : df.population
        }

# Create a dropdown Select widget: select    
select = Select(title="distribution", options=['female_literacy', 'population'], value='female_literacy')

# Attach the update_plot callback to the 'value' property of select
select.on_change('value', update_plot)

# Create layout and add to current document
layout = row(select, plot)
curdoc().add_root(layout)
