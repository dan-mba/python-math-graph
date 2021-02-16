"""
build_graph()
imputs:
  x_coordinates
  y_coordinates
  split_neg - when True, plots positive & negative x points seperately
output:
  graph formatted as a png data image

https://technovechno.com/creating-graphs-in-python-using-matplotlib-flask-framework-pythonanywhere/
"""

import numpy as np
import base64
import io
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('Agg')


def build_graph(x_coordinates, y_coordinates, split_neg=False):
    img = io.BytesIO()
    if split_neg:
        pos = np.flatnonzero(x_coordinates > 0)[0]
        plt.plot(x_coordinates[:pos], y_coordinates[:pos], color='b')
        plt.plot(x_coordinates[pos:], y_coordinates[pos:], color='b')
    else:
        plt.plot(x_coordinates, y_coordinates, color='b')
    plt.savefig(img, format='png')
    img.seek(0)
    graph_url = base64.b64encode(img.getvalue()).decode()
    plt.close()
    return 'data:image/png;base64,{}'.format(graph_url)
