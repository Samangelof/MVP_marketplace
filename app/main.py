from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.api.models import Item

app = FastAPI()

# Получение сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/test/db")
def test_db_connection(db: Session = Depends(get_db)):
    # Получаем все элементы из таблицы Item в базе данных
    items = db.query(Item).all()
    return {"message": "Подключение к базе данных успешно", "items": items}
