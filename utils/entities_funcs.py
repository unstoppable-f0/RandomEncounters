from typing import Type

from db.sql_queries import read_all_entities_by_type
from db.tables import SQLEntity


def print_all_entities(entity: Type[SQLEntity]):
    """Print all entities ids and names"""

    all_entities = read_all_entities_by_type(entity)

    if all_entities:
        for loc in all_entities:
            print(f'{loc.id}. {loc.name}')
    else:
        print('No entries')
    print("\n")


def get_all_entities_ids_and_print(entity: Type[SQLEntity]) -> list[int]:
    """Get all ids of entities and print ids and names in a proper manner."""

    all_locs = read_all_entities_by_type(entity)
    all_locs_ids = [loc.id for loc in all_locs]

    for loc in all_locs:
        print(f'{loc.id}. {loc.name}')
    print('\n')

    return all_locs_ids
