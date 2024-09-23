from typing import Type

from sqlalchemy import select, delete, update, text, any_, or_
from sqlalchemy.orm import sessionmaker

from db.connector import engine
from db.tables import SQLEntity, Encounter


Session = sessionmaker(bind=engine)


def read_an_entity(id_: int, entity_type: Type[SQLEntity]) -> SQLEntity:
    """Read an entity and return it."""

    with Session() as session:
        fetched_entity = session.get(entity_type, id_)
        return fetched_entity


def read_all_entities_by_type(entity: Type[SQLEntity]) -> list[Type[SQLEntity]]:
    with Session() as session:
        all_locs = session.query(entity).all()

        return all_locs


def create_entity(entity: SQLEntity) -> None:
    """Adds a new entity to the database."""
    with Session() as session:
        session.add(entity)
        session.commit()


def update_entity(entity: Type[SQLEntity], entity_id: int, update_values: dict) -> None:
    """Changes an existing entity."""

    with Session() as session:
        stmt = update(entity).where(entity.id == entity_id).values(update_values)
        session.execute(stmt)
        session.commit()


def delete_entity(entity: Type[SQLEntity], entity_id: int) -> None:
    """Deletes an existing entity."""

    with Session() as session:
        stmt = delete(entity).where(entity.id == entity_id)
        session.execute(stmt)
        session.commit()


def delete_all_entities(entity: Type[SQLEntity]) -> None:
    """Delete every row (truncate) from the entity's table."""

    table_name = entity.__name__.lower()

    with Session() as session:
        stmt = text(f"""TRUNCATE TABLE random_encs.public.{table_name}""")
        session.execute(stmt)
        session.commit()


def read_random_encounter(loc_id: int, time_id: int, weather_id: int) -> list[Encounter]:
    """Gets a random Encounter from the database."""

    with Session() as session:
        # somehow PyCharm thinks that any_(...) - is a wrong expression. idk, can make a ticket to JetBrains
        stmt = select(Encounter).where(or_(Encounter.time == time_id, Encounter.time == 3),
                                       any_(Encounter.locations) == loc_id,
                                       any_(Encounter.weather) == weather_id,
                                       Encounter.done == False
                                       )
        result = session.execute(stmt)

        fitting_encounters: list[Encounter] = [result[0] for result in result]
        return fitting_encounters
