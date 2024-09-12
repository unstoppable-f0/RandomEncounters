from db.sql_queries import get_all_locations


def print_all_locations():
    """Print all locations"""

    for loc in get_all_locations():
        print(f'{loc.id}. {loc.name}')
    print("\n")


def get_all_loc_ids_and_print() -> list[int]:
    """Get all ids of locations and print them in a proper manner."""

    all_locs = get_all_locations()
    all_locs_ids = [loc.id for loc in all_locs]

    for loc in all_locs:
        print(f'{loc.id}. {loc.name}')
    print('\n')

    return all_locs_ids
