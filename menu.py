from db.tables import Location, Weather, Encounter

from db.sql_queries import (
    create_entity,
    update_entity,
    delete_entity,
    delete_all_entities,
)

from utils.entities_funcs import print_all_entities, get_all_entities_ids_and_print


# ### Location part ###


def location_menu() -> None:
    """Calling a location menu"""

    print("Locations Options: "
          "\n1. Get all locations"
          "\n2. Add a new location"
          "\n3. Change locations"
          "\n4. Delete a locations"
          "\n5. Delete all locations"
          "\n6. Go back\n")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            location_dict[choice](Location)
        else:
            location_dict[choice]()
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

    choice = input("Are you sure you want to delete all locations? (y/n): ")
    if choice == 'y':
        delete_all_entities(Location)
        print("All locations deleted successfully")
    elif choice == 'n':
        print("Ok, going back to the main menu")
    else:
        print("Invalid input. Going back to the main menu")


# ### Weather part ###


def weather_menu() -> None:
    """Calling a weather menu"""

    print("Weather Options: "
          "\n1. Get every weather"
          "\n2. Add new weather"
          "\n3. Change weather"
          "\n4. Delete a weather"
          "\n5. Delete all weather"
          "\n6. Go back\n")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            weather_dict[choice](Weather)
        else:
            weather_dict[choice]()
    except (ValueError, KeyError):
        print("Invalid input. Please try again.\n")


def add_weather_menu() -> None:
    """Sub-menu for adding a weather"""

    new_weather = Weather()
    new_weather.name = input("Enter the name of the weather: ")
    create_entity(new_weather)
    print("Weather Added Successfully")


def change_weather_menu() -> None:
    """Sub-menu for changing a weather"""

    all_weather_ids = get_all_entities_ids_and_print(Weather)

    try:
        weather_id = int(input("Enter the weather id to change: "))
        if weather_id in all_weather_ids:
            new_values_dict = {'name': input("Enter the new name of the location: ")}
            update_entity(Weather, weather_id, new_values_dict)
            print("Weather Changed Successfully. Going back to the Weather menu")
        else:
            print('No weather with such id was found. Going back to the weather menu\n')
    except ValueError:
        print("Invalid input. Going back to the weather menu")


def delete_weather_menu() -> None:
    """Sub-menu for deleting a weather."""

    all_weather_ids = get_all_entities_ids_and_print(Weather)

    try:
        weather_id = int(input("Enter the weather id to delete: "))
        if weather_id in all_weather_ids:
            delete_entity(Weather, weather_id)
            print("Weather deleted successfully. Going back to the weather menu")
        else:
            print('No weather with such id was found. Going back to the weather menu\n')
    except ValueError:
        print("Invalid input. Going back to the weather menu")


def delete_all_weather_menu() -> None:
    """Sub-menu for deleting all weather."""

    choice = input("Are you sure you want to delete all weather? (y/n): ")
    if choice == 'y':
        delete_all_entities(Weather)
        print("All weather deleted successfully")
    elif choice == 'n':
        print("Ok, going back to the main menu")
    else:
        print("Invalid input. Going back to the main menu")


# ### Encounters part ###


def encounter_menu() -> None:
    """Calling a encounters menu"""

    print("Encounters Options: "
          "\n1. Get all encounters"
          "\n2. Add a new encounter"
          "\n3. Change an encounter"
          "\n4. Delete an encounter"
          "\n5. Delete all encounters"
          "\n6. Go back\n")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            encounter_dict[choice](Encounter)
        else:
            encounter_dict[choice]()
    except (ValueError, KeyError):
        print("Invalid input. Please try again.\n")


def add_encounter() -> None:
    """Adds a new encounter to the database."""

    new_encounter = Encounter()
    print('press Ctrl+D to break the app')

    # name part
    new_encounter.name = input('Enter encounter name: ')

    # time part
    print('Choose the time of day:\n'
          'Day - 1\n'
          'Night - 2\n'
          'Both - 3\n'
          '(choose only one!)')

    time_of_day = input(': ')
    # time validation
    if len(time_of_day) == 1 and time_of_day in ('1', '2', '3'):
        new_encounter.time = int(time_of_day)
    else:
        print('Wrong input. Returning to main menu')

    # locations part
    all_locs_ids = get_all_entities_ids_and_print(Location)
    user_locs = input('Choose id(s) of location(s) of the encounter (separated by space if many): ').split()

    if set(all_locs_ids).issuperset(set(user_locs)) and len(user_locs) >= 1:
        new_encounter.locations = map(int, user_locs)
    else:
        print('Wrong input. Returning to main menu')

    # weather part
    all_weather_ids = get_all_entities_ids_and_print(Weather)
    user_weather = input('Choose id(s) of weather of the encounter (separated by space if many): ').split()

    if set(all_weather_ids).issuperset(set(user_weather)) and len(user_weather) >= 1:
        new_encounter.weather = map(int, user_weather)
    else:
        print('Wrong input. Returning to main menu')

    # link part
    user_link = input('')












def delete_all_encounter_menu() -> None:
    """Deleting all rows of encounters"""

    choice = input("Are you sure you want to delete all encounters? (y/n): ")
    if choice == 'y':
        delete_all_entities(Encounter)
        print("All weather deleted successfully")
    elif choice == 'n':
        print("Ok, going back to the main menu")
    else:
        print("Invalid input. Going back to the main menu")


def main_menu() -> None:
    """Main menu function"""

    print("Welcome to the Main Menu. Choose an option: "
          "\n1. Get an encounter"
          "\n2. Encounters"
          "\n3. Locations"
          "\n4. Weather"
          "\n5. Exit\n")

    try:
        choice = int(input("Enter your choice: "))
        main_menu_dict[choice]()
    except (ValueError, KeyError):
        print("Invalid input. Please try again.\n")


# ### menu dicts ###

main_menu_dict = {
    2: encounter_menu,
    3: location_menu,
    4: weather_menu,
}

location_dict = {
    1: print_all_entities,
    2: add_location_menu,
    3: change_location_menu,
    4: delete_location_menu,
    5: delete_all_location_menu,
    6: main_menu
}

weather_dict = {
    1: print_all_entities,
    2: add_weather_menu,
    3: change_weather_menu,
    4: delete_weather_menu,
    5: delete_all_weather_menu,
    6: main_menu
}

encounter_dict = {
    1: print_all_entities,
    5: delete_all_encounter_menu
}

if __name__ == '__main__':
    main_menu()
