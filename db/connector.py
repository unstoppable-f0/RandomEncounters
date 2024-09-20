from sqlalchemy import create_engine
# from tables import Weather, Base, Encounter


engine = create_engine('postgresql+psycopg://iloginov:postgres@localhost:5433/random_encs')


if __name__ == '__main__':

    # Base.metadata.create_all(engine)
    # Base.metadata.drop_all(engine)
    # Encounter.__table__.drop(engine)
    pass
