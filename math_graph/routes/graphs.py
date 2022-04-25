from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from ..graph import build_graph
import numpy as np

router = APIRouter()


@router.get('/quad/{a}/{b}')
def graph_quad(a: int, b: int):
    x_values = np.arange(-5, 5, 0.01)
    y_values = (a * np.power(x_values, 2)) + (b * x_values)
    return RedirectResponse(build_graph(x_values, y_values))


@router.get('/pow/{a}/{b}')
def graph_pow(a: int, b: int):
    if b >= 0:
        x_values = np.concatenate(
            (np.arange(-5, -.01, 0.01), np.arange(.01, 5, .01)))
    else:
        x_values = np.concatenate(
            (np.arange(-.1, -.01, 0.001), np.arange(.01, .1, .001)))
    y_values = (a * np.power(x_values, b))
    return RedirectResponse(build_graph(x_values, y_values, True))


@router.get('/exp/{a}/{b}')
def graph_exp(a: int, b: int):
    x_values = np.arange(-5, 5, 0.01)
    y_values = (a * np.power(b, x_values))
    return RedirectResponse(build_graph(x_values, y_values, True))


@router.get('/expf/{a}/{b}')
def graph_expf(a: int, b: int):
    x_values = np.arange(-5, 5, 0.01)
    y_values = (a * np.power((1/b), x_values))
    return RedirectResponse(build_graph(x_values, y_values, True))


@router.get('/ln/{a}/{b}')
def graph_ln(a: int, b: int):
    x_values = np.arange(0.01, 10, 0.01)
    y_values = (a * np.log(x_values) + b)
    return RedirectResponse(build_graph(x_values, y_values, True))


@router.get('/log/{a}/{b}')
def graph_log(a: int, b: int):
    x_values = np.arange(0.01, 10, 0.01)
    y_values = (a * np.log10(x_values) + b)
    return RedirectResponse(build_graph(x_values, y_values, True))
