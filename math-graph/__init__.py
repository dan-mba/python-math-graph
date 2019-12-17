from flask import Flask, render_template, Response, redirect
from werkzeug.routing import IntegerConverter

app = Flask(__name__)

class SignedIntConverter(IntegerConverter):
  regex = r'-?\d+'

app.url_map.converters['signed_int'] = SignedIntConverter


@app.route('/')
def home():
  return render_template('home.html')

@app.route('/<string:fn>/<signed_int:coef>')
def graph_fn(fn, coef):
  image = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="
  url = f"data:image/png;base64,{image}"
  return redirect(url)
