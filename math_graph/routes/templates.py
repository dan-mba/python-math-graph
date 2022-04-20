from os import path
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()

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
    return templates.TemplateResponse('waves.html', {"request": request, "wave": wave})


@router.get('/curves', response_class=HTMLResponse)
def curves(request: Request):
    return templates.TemplateResponse('curves.html', {"request": request})
