from sqlalchemy import delete, update, text
from typing import Type

from sqlalchemy.orm import sessionmaker

from db.connector import engine
from db.tables import SQLEntity


Session = sessionmaker(bind=engine)


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
