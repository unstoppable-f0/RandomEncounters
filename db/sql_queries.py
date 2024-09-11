from sqlalchemy import delete

from sqlalchemy.orm import sessionmaker

from db.connector import engine
from db.tables import Weather, Location, Encounter

Session = sessionmaker(bind=engine)


def add_location(location: str) -> None:
    """Adds a new location to the location table."""

    with Session() as session:
        session.add(Location(name=location))
        session.commit()


def delete_location() -> None:
    """Deletes a location from the location table."""
    with Session() as session:
        stmt = delete(Location).where(Location.id == 2)
        session.execute(stmt)
        session.commit()

# add_location('Southern Stranglethorn Valley')
delete_location()
