from fastapi import APIRouter
from fastapi.responses import JSONResponse
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.embed import json_item
import numpy as np

router = APIRouter()
N = 400
line_color = '#4682b4'


@router.get('/ln/{a}/{b}')
def graph_ln(a: int, b: int):
    x_values = np.linspace(0.01, 10, N)
    y_values = (a * np.log(x_values) + b)
    source = ColumnDataSource(data=dict(x=x_values, y=y_values))

    plot = figure(height=600, width=600, x_range=[-0.1, 10.1])
    plot.line('x', 'y', source=source, line_width=3, line_color=line_color)
    return JSONResponse(content=json_item(plot))


@router.get('/log/{a}/{b}')
def graph_log(a: int, b: int):
    x_values = np.linspace(0.01, 10, N)
    y_values = (a * np.log10(x_values) + b)
    source = ColumnDataSource(data=dict(x=x_values, y=y_values))

    plot = figure(height=600, width=600, x_range=[-0.1, 10.1])
    plot.line('x', 'y', source=source, line_width=3, line_color=line_color)
    return JSONResponse(content=json_item(plot))
