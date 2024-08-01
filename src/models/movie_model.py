from fastapi import FastAPI, Body,Path,Query
from fastapi.responses import HTMLResponse,JSONResponse,PlainTextResponse,RedirectResponse,FileResponse
from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

#Modelos de datos
#Creamos una clase para crear las peliculas

class Movie(BaseModel):

#id: Optional[int] = None El id se vuelve opcional

    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str


# Validacion de datos
class MovieCreate(BaseModel):

    id: int
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50 )
    year: int = Field(le=datetime.date.today().year)# El año debe ser menor o igual al año actual
    rating: float = Field(ge=0, le=10)
    category: str = Field(min_length=5,max_length=20)
#category: str = Field(min_length=5,max_length=20,default='Aventura')#default es para poner un valor por defecto

    model_config = {#Se configuran estos valores como por defecto
        'json_schema_extra': {
            'example': {
            'id': 1,
            'title': 'my movie',
            'overview': 'Esta pelidula trata de',
            'year': 2022,
            'rating': 5,
            'category': 'Comedia'
                 } 
            }
        }


class MovieUpdate(BaseModel):

    title: str
    overview: str
    year: int
    rating: float
    category: str


#model config hacer ejemplos para valores por defecto






