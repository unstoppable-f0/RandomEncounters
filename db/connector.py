from sqlalchemy import create_engine

from db.tables import Base, Encounter, Location, Weather

engine = create_engine('postgresql+psycopg://iloginov:postgres@localhost:5433/random_encs')

Base.metadata.create_all(engine)
# Base.metadata.drop_all(engine)
# Location.__table__.drop(engine)
