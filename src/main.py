#Importaciones
from fastapi import FastAPI, Request, Response,Depends
from fastapi.responses import JSONResponse, PlainTextResponse
from src.routers.movie_router import movie_router
from src.utils.http_error_handler import HTTPErrorHandler
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()


app.add_middleware(HTTPErrorHandler)

#Moteores de plantillas
static_path = os.path.join(os.path.dirname(__file__), 'static/')
templates_path = os.path.join(os.path.dirname(__file__), 'templates/')

#Configuracion templates
app.mount('/static', StaticFiles(directory=static_path), 'static')
templates = Jinja2Templates(directory=templates_path)


#Titulos y version de la app
app.title = "Mi primera aplicacion con FastAPI"
app.version = "2.0.0"



@app.get('/', tags=['Home'])
def home(request: Request):
    return templates.TemplateResponse('index.html',{'request': request, 'message':'Welcome'})


#dependencias / inyeccion de codigo
def common_params(start_date:str, end_date: str):
    return{"start_date": start_date, "end_date": end_date}


@app.get('/users')
def get_users(commons: dict = Depends(common_params)):#utilizo la dependencia que me retorna las fechas de inicio y fin
    return f"user created between {commons ['start_date']} and {commons['end_date']}"


app.include_router(prefix='/movies', router=movie_router)
 


"""" Middleware 
@app.middleware('http')
async def http_error_handler( request: Request, call_next) -> Response | JSONResponse:
    print('Middleware is running')
    return await call_next(request)
"""  