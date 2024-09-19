from db.tables import Weather
from db.sql_queries import (
    create_entity,
    update_entity,
    delete_entity,
    delete_all_entities,
)

from utils.entities_funcs import print_all_entities, get_all_entities_ids_and_print


def weather_menu() -> None:
    """Calling a weather menu"""

    while True:
        print("Weather Options: "
              "\n1. Get every weather"
              "\n2. Add new weather"
              "\n3. Change weather"
              "\n4. Delete a weather"
              "\n5. Delete all weather"
              "\n6. Go back\n")

        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice == 1:
                weather_dict[user_choice](Weather)
            elif user_choice == 6:
                break
            else:
                weather_dict[user_choice]()
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

    user_choice = input("Are you sure you want to delete all weather? (y/n): ")
    if user_choice == 'y':
        delete_all_entities(Weather)
        print("All weather deleted successfully")
    elif user_choice == 'n':
        print("Ok, going back to the main menu")
    else:
        print("Invalid input. Going back to the main menu")


weather_dict = {
    1: print_all_entities,
    2: add_weather_menu,
    3: change_weather_menu,
    4: delete_weather_menu,
    5: delete_all_weather_menu,
}
