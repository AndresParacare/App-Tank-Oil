import os
import sqlalchemy as db
import persistence.model as mod

# Ensure the directory for the SQLite database file exists
db_directory = './cache/db'
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

# Permite crear el motor de la base de datos
engine = db.create_engine('sqlite:///./cache/db/login.sqlite', echo=True, future=True)
mod.Base.metadata.create_all(engine)
