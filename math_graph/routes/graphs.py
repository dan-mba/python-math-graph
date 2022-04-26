from fastapi import APIRouter
from fastapi.responses import JSONResponse
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.embed import json_item
import numpy as np

router = APIRouter()
N = 400

@router.get('/quad/{a}/{b}')
def graph_quad(a: int, b: int):
    x_values = np.linspace(-2, 2, N)
    y_values = (a * np.power(x_values, 2)) + (b * x_values)
    source = ColumnDataSource(data=dict(x=x_values, y=y_values))

    plot = figure(height=600, width=600, x_range=[-2.1, 2.1])
    plot.line('x', 'y', source=source, line_width=3, line_color='#14134c')
    return JSONResponse(content=json_item(plot))


@router.get('/pow/{a}/{b}')
def graph_pow(a: int, b: int):
    if b >= 0:
        x_values = np.concatenate(
            (np.linspace(-2, -.01, round(N/2)), np.linspace(.01, 2, round(N/2))))
        x_range = [-2.1, 2.1]
    else:
        x_values = np.concatenate(
            (np.linspace(-.02, -.001, round(N/2)), np.linspace(.001, .02, round(N/2))))
        x_range = [-.021, .021]
    y_values = (a * np.power(x_values, b))
    source = ColumnDataSource(data=dict(x=x_values, y=y_values))

    plot = figure(height=600, width=600, x_range=x_range)
    plot.line('x', 'y', source=source, line_width=3, line_color='#14134c')
    return JSONResponse(content=json_item(plot))
