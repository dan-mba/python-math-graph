from fastapi import APIRouter
from fastapi.responses import JSONResponse
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.embed import json_item
import numpy as np

router = APIRouter()
N = 200
line_color = '#4682b4'

@router.get('/sin/{freq}')
def graph_sine(freq: int):
    x_values = np.linspace(-2*np.pi, 2*np.pi, N)
    y_values = np.sin(x_values*freq)
    source = ColumnDataSource(data=dict(x=x_values, y=y_values))

    plot = figure(height=600, width=600, x_range=[-2*np.pi, 2*np.pi], y_range=[-1.5, 1.5])
    plot.line('x', 'y', source=source, line_width=3, line_color=line_color)
    return JSONResponse(content=json_item(plot))


@router.get('/cos/{freq}')
def graph_cosine(freq: int):
    x_values = np.linspace(-2*np.pi, 2*np.pi, N)
    y_values = np.cos(x_values*freq)
    source = ColumnDataSource(data=dict(x=x_values, y=y_values))

    plot = figure(x_range=[-2*np.pi, 2*np.pi], y_range=[-1.5, 1.5])
    plot.line('x', 'y', source=source, line_width=3, line_color=line_color)
    return JSONResponse(content=json_item(plot))
