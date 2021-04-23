from os import path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from .graph import build_graph
import numpy as np

app = FastAPI()

app.mount("/static", StaticFiles(directory=path.join(path.dirname(__file__),
          "static")), name="static")

templates = Jinja2Templates(directory=path.join(
    path.dirname(__file__), "templates"))


@app.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('home.html', {"request": request})


@app.get('/waves', response_class=HTMLResponse)
def waves(request: Request):
    return templates.TemplateResponse('waves.html', {"request": request})


@app.get('/curves', response_class=HTMLResponse)
def curves(request: Request):
    return templates.TemplateResponse('curves.html', {"request": request})


@app.get('/sin/{freq}')
def graph_sine(freq: int):
    x_values = np.arange(-5, 5, 0.01)
    y_values = np.sin(x_values*freq)
    return RedirectResponse(build_graph(x_values, y_values))


@app.get('/cos/{freq}')
def graph_cosine(freq: int):
    x_values = np.arange(-5, 5, 0.01)
    y_values = np.cos(x_values*freq)
    return RedirectResponse(build_graph(x_values, y_values))


@app.get('/quad/{a}/{b}')
def graph_quad(a: int, b: int):
    x_values = np.arange(-5, 5, 0.01)
    y_values = (a * np.power(x_values, 2)) + (b * x_values)
    return RedirectResponse(build_graph(x_values, y_values))


@app.get('/pow/{a}/{b}')
def graph_pow(a: int, b: int):
    if b >= 0:
        x_values = np.concatenate(
            (np.arange(-5, -.01, 0.01), np.arange(.01, 5, .01)))
    else:
        x_values = np.concatenate(
            (np.arange(-.1, -.01, 0.001), np.arange(.01, .1, .001)))
    y_values = (a * np.power(x_values, b))
    return RedirectResponse(build_graph(x_values, y_values, True))


@app.get('/exp/{a}/{b}')
def graph_exp(a: int, b: int):
    x_values = np.arange(-5, 5, 0.01)
    y_values = (a * np.power(b, x_values))
    return RedirectResponse(build_graph(x_values, y_values, True))


@app.get('/expf/{a}/{b}')
def graph_expf(a: int, b: int):
    x_values = np.arange(-5, 5, 0.01)
    y_values = (a * np.power((1/b), x_values))
    return RedirectResponse(build_graph(x_values, y_values, True))


@app.get('/ln/{a}/{b}')
def graph_ln(a: int, b: int):
    x_values = np.arange(0.01, 10, 0.01)
    y_values = (a * np.log(x_values) + b)
    return RedirectResponse(build_graph(x_values, y_values, True))


@app.get('/log/{a}/{b}')
def graph_log(a: int, b: int):
    x_values = np.arange(0.01, 10, 0.01)
    y_values = (a * np.log10(x_values) + b)
    return RedirectResponse(build_graph(x_values, y_values, True))
