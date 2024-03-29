from fastapi import APIRouter
from fastapi.responses import JSONResponse
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.embed import json_item
import numpy as np

router = APIRouter()
N = 400
line_color = '#4682b4'


@router.get('/quad/{a}/{b}')
def graph_quad(a: int, b: int):
    x_values = np.linspace(-2, 2, N)
    y_values = (a * np.power(x_values, 2)) + (b * x_values)
    source = ColumnDataSource(data=dict(x=x_values, y=y_values))

    plot = figure(height=600, width=600, x_range=[-2.1, 2.1])
    plot.line('x', 'y', source=source, line_width=3, line_color=line_color)
    return JSONResponse(content=json_item(plot))


@router.get('/pow/{a}/{b}')
def graph_pow(a: int, b: int):
    if b >= 0:
        x_values = np.linspace(-2, 2, N)
        y_values = (a * np.power(x_values, b))
        source = ColumnDataSource(data=dict(x=x_values, y=y_values))

        plot = figure(height=600, width=600, x_range=[-2.1, 2.1])
        plot.line('x', 'y', source=source, line_width=3, line_color=line_color)
    else:
        x_values_neg = np.linspace(-.01, -.0001, round(N/2))
        x_values_pos = np.linspace(.0001, .01, round(N/2))
        x_range = [-.011, .011]
        y_values_pos = (a * np.power(x_values_pos, b))
        y_values_neg = (a * np.power(x_values_neg, b))
        source_neg = ColumnDataSource(
            data=dict(x=x_values_neg, y=y_values_neg))
        source_pos = ColumnDataSource(
            data=dict(x=x_values_pos, y=y_values_pos))

        plot = figure(height=600, width=600, x_range=x_range)
        plot.line('x', 'y', source=source_neg,
                  line_width=3, line_color=line_color)
        plot.line('x', 'y', source=source_pos,
                  line_width=3, line_color=line_color)

    return JSONResponse(content=json_item(plot))
