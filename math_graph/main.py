from os import path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .routes import templates
from .routes import graphs
from .routes import wave_graphs

app = FastAPI()

app.mount("/static", StaticFiles(directory=path.join(path.dirname(__file__),
          "static")), name="static")

app.include_router(templates.router)
app.include_router(graphs.router)
app.include_router(wave_graphs.router)
