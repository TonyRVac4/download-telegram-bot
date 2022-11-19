from peewee import *
from config_data.config import DATA_BASE_PATH


db = SqliteDatabase(DATA_BASE_PATH)


class BaseModel(Model):
    class Meta:
        database = db


class History(BaseModel):
    user_id = IntegerField()
    file_path = TextField()
    type = TextField()
