from sqlalchemy import delete, update, text
from typing import Type

from sqlalchemy.orm import sessionmaker

from db.connector import engine
from db.tables import Weather, Location, Encounter


Session = sessionmaker(bind=engine)

# ### Location part ###


def get_all_locations() -> list[Type[Location]]:
    """Get a list of all locations."""

    with Session() as session:
        all_locs = session.query(Location).all()

        return all_locs


def add_location(location: str) -> None:
    """Adds a new location to the location table."""

    with Session() as session:
        session.add(Location(name=location))
        session.commit()


def change_location(loc_id: int, new_loc_name: str) -> None:
    """Changes a location in the location table."""

    with Session() as session:
        stmt = update(Location).where(Location.id == loc_id).values(name=new_loc_name)
        session.execute(stmt)
        session.commit()


def delete_location(loc_id: int) -> None:
    """Deletes a location from the location table."""

    with Session() as session:
        stmt = delete(Location).where(Location.id == loc_id)
        session.execute(stmt)
        session.commit()


def delete_all_location() -> None:
    """Delete every row (truncate) from the location table."""

    with Session() as session:
        stmt = text("""TRUNCATE TABLE random_encs.public.location""")
        session.execute(stmt)
        session.commit()


# ### Weather part ###


def get_all_weather() -> list[Type[Weather]]:
    """Get a list of all locations."""

    with Session() as session:
        all_weather = session.query(Weather).all()

        return all_weather


def add_weather(weather: str) -> None:
    """Adds a new weather to the weather table."""

    with Session() as session:
        session.add(Weather(name=weather))
        session.commit()


def change_weather(weather_id: int, new_weather_name: str) -> None:
    """Changes a weather in the weather table."""

    with Session() as session:
        stmt = update(Weather).where(Weather.id == weather_id).values(name=new_weather_name)
        session.execute(stmt)
        session.commit()


def delete_weather(weather_id: int) -> None:
    """Deletes a weather from the weather table."""

    with Session() as session:
        stmt = delete(Weather).where(Weather.id == weather_id)
        session.execute(stmt)
        session.commit()


def delete_all_weather() -> None:
    """Delete every row (truncate) from the weather table."""

    with Session() as session:
        stmt = text("""TRUNCATE TABLE random_encs.public.weather""")
        session.execute(stmt)
        session.commit()


# ### Encounters Part ###


def get_all_encounters() -> list[Type[Encounter]]:
    """Get a list of all encounters."""

    with Session() as session:
        all_encounters = session.query(Encounter).all()

        return all_encounters


def add_encounter(weather: str) -> None:
    """Adds a new encounter to the weather table."""

    with Session() as session:
        session.add(Weather(name=weather))
        session.commit()