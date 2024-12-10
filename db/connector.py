from sqlalchemy import create_engine
from db.settings import DBSettings

db_settings = DBSettings()
engine = create_engine(db_settings.dsn)
