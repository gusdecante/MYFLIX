from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config import database
from src.schemas import schemas
from src.infra.sqlalchemy.repositories.series import RepositorySerie

database.create_db()

app = FastAPI()

@app.post('/series')
def create_serie(serie: schemas.Serie, database: Session = Depends(database.get_db)):
  created_serie = RepositorySerie(database).create(serie)
  return created_serie

@app.get('/series')
def list_series(database: Session = Depends(database.get_db)):
  return RepositorySerie(database).index()

@app.get('/series/{serie_id}')
def get_serie(serie_id: int, database: Session = Depends(database.get_db)):
  serie = RepositorySerie(database).get(serie_id)
  return serie

@app.delete('/series/{serie_id}')
def delete_serie(serie_id: int, database: Session = Depends(database.get_db)):
  serie = RepositorySerie(database).delete(serie_id)
  return {"mensagem": "removido com sucesso"}