"""
build_graph()
imputs:
  x_coordinates
  y_coordinates
output:
  graph formatted as a png data image

https://technovechno.com/creating-graphs-in-python-using-matplotlib-flask-framework-pythonanywhere/
"""

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import io
import base64
 
def build_graph(x_coordinates, y_coordinates):
  img = io.BytesIO()
  plt.plot(x_coordinates, y_coordinates)
  plt.savefig(img, format='png')
  img.seek(0)
  graph_url = base64.b64encode(img.getvalue()).decode()
  plt.close()
  return 'data:image/png;base64,{}'.format(graph_url)
