from os import path
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from bokeh.resources import CDN

router = APIRouter()

js_resources = CDN.render_js()

wavesList = ['sin', 'cos']
curvesList = ['quad', 'pow', 'exp', 'expf', 'ln', 'log']
bZero = ['quad', 'ln', 'log']

templates = Jinja2Templates(directory=path.join(
    path.dirname(__file__), "templates"))


@router.get('/', response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse('home.html', {"request": request})


@router.get('/waves', response_class=RedirectResponse)
def waveRedirect():
    return "/waves/sin"


@router.get('/waves/{wave}', response_class=HTMLResponse)
def waves(wave: str, request: Request):

    try:
        waveIndex = wavesList.index(wave)
    except ValueError:
        raise HTTPException(status_code=404, detail="Wave not found")
    return templates.TemplateResponse('waves.html',
                                      {
                                          "request": request,
                                          "wave": wave,
                                          "js_resources": js_resources
                                      })


@router.get('/curves', response_class=RedirectResponse)
def curveRedirect():
    return "/curves/quad"


@router.get('/curves/{curve}', response_class=HTMLResponse)
def curves(curve: str, request: Request):
    try:
        curveIndex = curvesList.index(curve)
    except ValueError:
        raise HTTPException(status_code=404, detail="Curve not found")

    b = 2
    if curve in bZero:
        b = 0
    elif curve == 'pow':
        b = 1

    return templates.TemplateResponse('curves.html',
                                      {
                                          "request": request,
                                          "curve": curve,
                                          "b": b,
                                          "js_resources": js_resources
                                      })
