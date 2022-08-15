
from peewee import *

db = PostgresqlDatabase(
    'countries',
    host = 'localhost',
    port = '5432',
    user = 'saske',
    password = 'qwe123'
)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class Info(BaseModel):
    name = CharField(max_length=255, null=False, unique=True)
    OfficalName = CharField(max_length=255, null=False, unique=True)
    capital = CharField(max_length=255, null=False, unique=True)
    region = CharField(max_length=255, null=False, unique=True)
    subregion = CharField(max_length=255, null=False, unique=True)
    population = CharField(max_length=255, null=False, unique=True)
    continent = CharField(max_length=255, null=False, unique=True)
    timezones = CharField(max_length=255, null=False, unique=True)

    def __repr__(self):
        return self.name

# db.create_tables([Info])

db.close()
