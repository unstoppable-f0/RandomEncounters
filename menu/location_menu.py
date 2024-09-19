from db.tables import Location
from db.sql_queries import (
    create_entity,
    update_entity,
    delete_entity,
    delete_all_entities,
)

from utils.entities_funcs import print_all_entities, get_all_entities_ids_and_print


def location_menu() -> None:
    """Calling a location menu"""

    while True:
        print("Locations Options: "
              "\n1. Get all locations"
              "\n2. Add a new location"
              "\n3. Change locations"
              "\n4. Delete a locations"
              "\n5. Delete all locations"
              "\n6. Go back\n")

        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice == 1:
                location_dict[user_choice](Location)
            elif user_choice == 6:
                break
            else:
                location_dict[user_choice]()
        except (ValueError, KeyError):
            print("Invalid input. Please try again.\n")


def add_location_menu() -> None:
    """sub-menu for adding a location"""

    new_location = Location()
    new_location.name = input("Enter the name of the location: ")
    create_entity(new_location)
    print("Location Added Successfully")


def change_location_menu() -> None:
    """Sub-menu for changing a location"""

    all_locs_ids = get_all_entities_ids_and_print(Location)

    try:
        loc_id = int(input("Enter the location id to change: "))
        if loc_id in all_locs_ids:
            new_values_dict = {'name': input("Enter the new name of the location: ")}
            update_entity(Location, loc_id, new_values_dict)
            print("Location Changed Successfully. Going back to the locations menu")
        else:
            print('No location with such id was found. Going back to the locations menu\n')
    except ValueError:
        print("Invalid input. Going back to the locations menu")


def delete_location_menu() -> None:
    """Sub-menu for deleting a location."""

    all_locs_ids = get_all_entities_ids_and_print(Location)

    try:
        loc_id = int(input("Enter the location id to delete: "))
        if loc_id in all_locs_ids:
            delete_entity(Location, loc_id)
            print("Location deleted successfully. Going back to the locations menu")
        else:
            print('No location with such id was found. Going back to the locations menu\n')
    except ValueError:
        print("Invalid input. Going back to the locations menu")


def delete_all_location_menu() -> None:
    """Sub-menu for deleting all locations."""

    user_choice = input("Are you sure you want to delete all locations? (y/n): ")
    if user_choice == 'y':
        delete_all_entities(Location)
        print("All locations deleted successfully")
    elif user_choice == 'n':
        print("Ok, going back to the main menu")
    else:
        print("Invalid input. Going back to the main menu")


location_dict = {
    1: print_all_entities,
    2: add_location_menu,
    3: change_location_menu,
    4: delete_location_menu,
    5: delete_all_location_menu,
}
