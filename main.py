from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from sqlalchemy.sql import text
from fastapi.encoders import jsonable_encoder

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
    result = db.execute(text("SELECT * FROM country")).fetchall()

    formatted_result = [list(row) for row in result]
    return jsonable_encoder(formatted_result)