from db.sql_queries import (
    add_location,
    change_location,
    delete_location,
    delete_all_location,
    add_weather,
    change_weather,
    delete_weather,
    delete_all_weather
)

from utils.location_funcs import print_all_locations, get_all_loc_ids_and_print
from utils.weather_funcs import print_all_weather, get_all_weather_ids_and_print


# ### Location part ###


def location_menu():
    """Calling a location menu"""

    print("Locations Options: "
          "\n1. Get all locations"
          "\n2. Add a location"
          "\n3. Change locations"
          "\n4. Delete a locations"
          "\n5. Delete all locations"
          "\n6. Go back\n")

    try:
        choice = int(input("Enter your choice: "))
        location_dict[choice]()
    except (ValueError, KeyError):
        print("Invalid input. Please try again.\n")


def add_location_menu():
    """sub-menu for adding a location"""

    location_name = input("Enter the name of the location: ")
    add_location(location_name)
    print("Location Added Successfully")


def change_location_menu():
    """Sub-menu for changing a location"""

    all_locs_ids = get_all_loc_ids_and_print()

    try:
        loc_id = int(input("Enter the location id to change: "))
        if loc_id in all_locs_ids:
            location_name = input("Enter the new name of the location: ")
            change_location(loc_id, location_name)
            print("Location Changed Successfully. Going back to the locations menu")
        else:
            print('No location with such id was found. Going back to the locations menu\n')
    except ValueError:
        print("Invalid input. Going back to the locations menu")


def delete_location_menu():
    """Sub-menu for deleting a location."""

    all_locs_ids = get_all_loc_ids_and_print()

    try:
        loc_id = int(input("Enter the location id to delete: "))
        if loc_id in all_locs_ids:
            delete_location(loc_id)
            print("Location deleted successfully. Going back to the locations menu")
        else:
            print('No location with such id was found. Going back to the locations menu\n')
    except ValueError:
        print("Invalid input. Going back to the locations menu")


def delete_all_location_menu():
    """Sub-menu for deleting all locations."""

    choice = input("Are you sure you want to delete all locations? (y/n): ")
    if choice == 'y':
        delete_all_location()
        print("All locations deleted successfully")
    elif choice == 'n':
        print("Ok, going back to the main menu")
    else:
        print("Invalid input. Going back to the main menu")


# ### Weather part ###


def weather_menu():
    """Calling a weather menu"""

    print("Weather Options: "
          "\n1. Get all weather"
          "\n2. Add one weather"
          "\n3. Change weather"
          "\n4. Delete a weather"
          "\n5. Delete all weather"
          "\n6. Go back\n")

    try:
        choice = int(input("Enter your choice: "))
        weather_dict[choice]()
    except (ValueError, KeyError):
        print("Invalid input. Please try again.\n")


def add_weather_menu():
    """Sub-menu for adding a weather"""

    weather_name = input("Enter the name of the weather: ")
    add_weather(weather_name)
    print("Weather Added Successfully")


def change_weather_menu():
    """Sub-menu for changing a weather"""

    all_weather_ids = get_all_weather_ids_and_print()

    try:
        weather_id = int(input("Enter the weather id to change: "))
        if weather_id in all_weather_ids:
            weather_name = input("Enter the new name of the weather: ")
            change_weather(weather_id, weather_name)
            print("Weather Changed Successfully. Going back to the Weather menu")
        else:
            print('No weather with such id was found. Going back to the weather menu\n')
    except ValueError:
        print("Invalid input. Going back to the weather menu")


def delete_weather_menu():
    """Sub-menu for deleting a weather."""

    all_weather_ids = get_all_weather_ids_and_print()

    try:
        weather_id = int(input("Enter the weather id to delete: "))
        if weather_id in all_weather_ids:
            delete_weather(weather_id)
            print("Weather deleted successfully. Going back to the weather menu")
        else:
            print('No weather with such id was found. Going back to the weather menu\n')
    except ValueError:
        print("Invalid input. Going back to the weather menu")


def delete_all_weather_menu():
    """Sub-menu for deleting all weather."""

    choice = input("Are you sure you want to delete all weather? (y/n): ")
    if choice == 'y':
        delete_all_weather()
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
          "\n2. Add one encounter"
          "\n3. Change an encounter"
          "\n4. Delete an encounter"
          "\n5. Delete all encounters"
          "\n6. Go back\n")

    try:
        choice = int(input("Enter your choice: "))
        encounter_dict[choice]()
    except (ValueError, KeyError):
        print("Invalid input. Please try again.\n")




def main_menu():
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
    1: print_all_locations,
    2: add_location_menu,
    3: change_location_menu,
    4: delete_location_menu,
    5: delete_all_location_menu,
    6: main_menu
}

weather_dict = {
    1: print_all_weather,
    2: add_weather_menu,
    3: change_weather_menu,
    4: delete_weather_menu,
    5: delete_all_weather_menu,
    6: main_menu
}

encounter_dict = {

}

if __name__ == '__main__':
    main_menu()
