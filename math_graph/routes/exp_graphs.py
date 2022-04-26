from fastapi import APIRouter
from fastapi.responses import JSONResponse
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.embed import json_item
import numpy as np

router = APIRouter()
N = 400


@router.get('/exp/{a}/{b}')
def graph_exp(a: int, b: int):
    x_values = np.linspace(-5, 5, N)
    y_values = (a * np.power(b, x_values))
    source = ColumnDataSource(data=dict(x=x_values, y=y_values))

    plot = figure(height=600, width=600, x_range=[-5.1, 5.1])
    plot.line('x', 'y', source=source, line_width=3, line_color='#14134c')
    return JSONResponse(content=json_item(plot))


@router.get('/expf/{a}/{b}')
def graph_expf(a: int, b: int):
    x_values = np.linspace(-5, 5, N)
    y_values = (a * np.power((1/b), x_values))
    source = ColumnDataSource(data=dict(x=x_values, y=y_values))

    plot = figure(height=600, width=600, x_range=[-5.1, 5.1])
    plot.line('x', 'y', source=source, line_width=3, line_color='#14134c')
    return JSONResponse(content=json_item(plot))

