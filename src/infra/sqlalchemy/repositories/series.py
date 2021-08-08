from sqlalchemy.orm import Session
from src.infra.sqlalchemy.models import models
from src.schemas import schemas

class RepositorySerie():
  def __init__(self, database: Session):
    self.database = database

  def create(self, serie: schemas.Serie):
    db_serie = models.Serie(title=serie.title, year=serie.year, gender=serie.gender, qtt_seasons=serie.qtt_seasons)
    
    self.database.add(db_serie)
    self.database.commit()
    self.database.refresh(db_serie)

    return db_serie

  def index(self):
    series = self.database.query(models.Serie).all()
    return series

  def get(self, serie_id: int):
    serie = self.database.query(models.Serie).filter(models.Serie.id == serie_id).one()

    return serie

  def delete(self, serie_id: int):
    serie = self.get(serie_id)

    self.database.delete(serie)
    self.database.commit()
