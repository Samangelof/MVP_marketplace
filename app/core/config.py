from pydantic import BaseSettings


class Settings(BaseSettings):
    db_username: str
    db_password: str
    db_host: str
    db_name: str

settings = Settings(
    db_username="Markovka",
    db_password="&B-!r6e=iTPftbg",
    db_host="localhost",
    db_name="mvp_marketplace"
)