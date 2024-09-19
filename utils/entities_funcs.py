from typing import Type

from db.sql_queries import read_all_entities_by_type
from db.tables import SQLEntity, Encounter


def entities_sorted_by_id(entity_list: list[Type[SQLEntity]]) -> list[Type[SQLEntity]]:
    """Sorts a list of entities by their id in ascending order."""

    return sorted(entity_list, key=lambda entity: entity.id)


def print_all_entities(entity_type: Type[SQLEntity]):
    """Print all entities ids and names"""

    all_entities = read_all_entities_by_type(entity_type)

    if all_entities:
        for entity in entities_sorted_by_id(all_entities):
            print(entity)
    else:
        print('No entries')
    print("\n")


def get_all_entities_ids_and_print(entity_type: Type[SQLEntity]) -> list[int]:
    """Get all ids of entities and print ids and names in a proper manner."""

    all_locs = read_all_entities_by_type(entity_type)
    all_locs_ids = [loc.id for loc in all_locs]

    for entity in entities_sorted_by_id(all_locs):
        print(entity)
    print('')

    return all_locs_ids
