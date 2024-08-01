from fastapi import Path, Query, APIRouter
from fastapi.responses import JSONResponse,PlainTextResponse,FileResponse
from typing import  List
from src.models.movie_model import Movie, MovieUpdate, MovieCreate



movies: List[Movie] = []


movie_router = APIRouter()


# Uso metodo Get
#Paramatros de ruta
#localhost:5000/movies/1
@movie_router.get('/', tags=['Movies'])
def get_movies()-> List[Movie]:
    content = [movie.model_dump() for movie in movies] 
    return JSONResponse(content=content,status_code=200)


@movie_router.get('/{id}', tags=['Movies'])
def get_movie(id: int = Path(gt=0)) -> Movie | dict:
    for movie in movies:
        if movie.id == id:
            return JSONResponse (movie.model_dump(),status_code=200)
    return JSONResponse(content={}, status_code=404 )    


#Parametro Query
#localhost:5000/movies/?id=1

@movie_router.get('/by_category', tags=['Movies'])
def get_movie_by_category(category: str = Query(min_length=5,max_length=20)) -> Movie | dict:
        for movie in movies:
            if movie.category== category:
                return JSONResponse (movie.model_dump(), status_code=200)
        return JSONResponse(content={}, status_code=404)


#Metodo Post

@movie_router.post('/', tags=['Movies'])
def create_movie(movie: MovieCreate) -> List[Movie]:
     movies.append(movie)
     content = [movie.model_dump() for movie in movies] 
     return JSONResponse(content=content, status_code=201)
     #return RedirectResponse('/movies',status_code=303)


#Metodo Put

@movie_router.put('/{id}', tags=['Movies'])
def update_movie(id: int, movie: MovieUpdate) -> List[Movie]:
     
    for item in movies:
        if item.id == id:
            item.title = movie.title
            item.overview = movie.overview
            item.year = movie.year
            item.rating = movie.rating
            item.category = movie.category
    content = [movie.model_dump() for movie in movies] 
    return JSONResponse(content=content, status_code=200)

#Metodo delete

@movie_router.delete('/{id}', tags=['Movies'])
def delete_movie(id: int) -> List[Movie]:
    for movie in movies:
        if movie.id == id:
            movies.remove(movie)
    content = [movie.model_dump() for movie in movies] 
    return JSONResponse(content=content, status_code=200)

# Obtener documento
"""" 
@app.get('/get_file', tags=['Documento'])
def get_file():
    return FileResponse('documento.pdf')
"""

