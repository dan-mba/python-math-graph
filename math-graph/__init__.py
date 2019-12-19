from flask import Flask, render_template, Response, redirect
from werkzeug.routing import IntegerConverter
from .graph import build_graph
import numpy as np

app = Flask(__name__)

class SignedIntConverter(IntegerConverter):
  regex = r'-?\d+'

app.url_map.converters['signed_int'] = SignedIntConverter


@app.route('/')
def home():
  return render_template('home.html')

@app.route('/waves')
def waves():
  return render_template('waves.html')

@app.route('/curves')
def curves():
  return render_template('curves.html')

@app.route('/sin/<signed_int:freq>')
def graph_sine(freq):
  x_values = np.arange(-5, 5, 0.01)
  y_values = np.sin(x_values*freq)
  return redirect(build_graph(x_values, y_values))

@app.route('/cos/<signed_int:freq>')
def graph_cosine(freq):
  x_values = np.arange(-5, 5, 0.01)
  y_values = np.cos(x_values*freq)
  return redirect(build_graph(x_values, y_values))

@app.route('/quad/<signed_int:a>/<signed_int:b>')
def graph_quad(a, b):
  x_values = np.arange(-5, 5, 0.01)
  y_values = (a * np.power(x_values, 2)) + (b * x_values)
  return redirect(build_graph(x_values, y_values))

@app.route('/pow/<signed_int:a>/<signed_int:b>')
def graph_pow(a, b):
  if b>=0:
    x_values = np.concatenate((np.arange(-5, -.01, 0.01), np.arange(.01, 5, .01)))
  else:
    x_values = np.concatenate((np.arange(-.1, -.01, 0.001), np.arange(.01, .1, .001)))
  y_values = (a * np.power(x_values, b))
  return redirect(build_graph(x_values, y_values))

"""
Function to return 1x1 transparent png
@app.route('/<string:fn>/<signed_int:coef>')
def graph_fn(fn, coef):
  image = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
  url = f"data:image/png;base64,{image}"
  return redirect(url)
"""
