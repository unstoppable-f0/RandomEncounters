from random import choice

from db.tables import Location, Weather, Encounter
from db.sql_queries import (
    create_entity,
    update_entity,
    delete_entity,
    delete_all_entities,
    read_random_encounter
)

from utils.entities_funcs import print_all_entities, get_all_entities_ids_and_print


def encounter_menu() -> None:
    """Calling a encounters menu"""

    while True:
        print("Encounters Options: "
              "\n1. Get all encounters"
              "\n2. Add a new encounter"
              "\n3. Change an encounter"
              "\n4. Delete an encounter"
              "\n5. Delete all encounters"
              "\n6. Go back\n")

        try:
            user_choice = int(input("Enter your choice: "))
            print()
            if user_choice == 1:
                encounter_dict[user_choice](Encounter)
            elif user_choice == 6:
                break
            else:
                encounter_dict[user_choice]()
        except (ValueError, KeyError):
            print("Invalid input. Please try again.\n")


def create_encounter_menu() -> None:
    """Adds a new encounter to the database."""

    new_encounter = Encounter()
    print("Let's create a new encounter!"
          "\n(press Ctrl+D to break the app)\n")

    # name part
    new_encounter.name = input('Enter encounter name: ')
    print('Got the name\n')

    # time part
    print('Choose the time of day:\n'
          'Day - 1\n'
          'Night - 2\n'
          'Both - 3\n'
          '(choose only one!)')

    time_of_day = input('Enter the time: ')
    # time validation
    if len(time_of_day) == 1 and time_of_day in ('1', '2', '3'):
        new_encounter.time = int(time_of_day)
        print('Got the time\n')
    else:
        print('Wrong input. Returning to main menu')

    # locations part
    print('Locations ids:')
    all_locs_ids = get_all_entities_ids_and_print(Location)
    try:
        user_locs = input('Choose id(s) of location(s) of the encounter (separated by space if many): ').split()
        user_locs = list(map(int, user_locs))
    except ValueError:
        print("Invalid input. Please try again.")
        return

    if set(all_locs_ids).issuperset(set(user_locs)) and len(user_locs) >= 1:
        new_encounter.locations = map(int, user_locs)
        print('Got the locations')
    else:
        print('Wrong input. Returning to main menu')
        return

    # weather part
    all_weather_ids = get_all_entities_ids_and_print(Weather)
    try:
        user_weather = input('Choose id(s) of weather of the encounter (separated by space if many): ').split()
        user_weather = list(map(int, user_weather))
    except ValueError:
        print('Invalid input. Returning to main menu')
        return

    if set(all_weather_ids).issuperset(set(user_weather)) and len(user_weather) >= 1:
        new_encounter.weather = user_weather
        print('Got the weather\n')
    else:
        print('Wrong input. Returning to main menu')
        return

    # link part
    new_encounter.link = input('Insert link for the encounter or just press enter to continue.'
                               '\n(you can always add it later)'
                               '\nEnter the link:')
    print()
    new_encounter.done = False

    # prerequisites-part
    # TODO prerequisites-part

    create_entity(new_encounter)
    print('Encounter added successfully!\n')


def update_encounter_menu() -> None:
    """Updates an encounter in the Encounters tables of DB."""

    user_choice = input('What do you want to change?')


def delete_all_encounter_menu() -> None:
    """Deleting all rows of encounters"""

    user_choice = input("Are you sure you want to delete all encounters? (y/n): ")
    if user_choice == 'y':
        delete_all_entities(Encounter)
        print("All weather deleted successfully")
    elif user_choice == 'n':
        print("Ok, going back to the main menu")
    else:
        print("Invalid input. Going back to the main menu")


# Read random Encounter menu


def read_random_enc_menu():
    """Menu for reading a random encounters"""

    print_all_entities(Location)
    loc_choice = int(input('Choose one location for the encounter: '))
    time_choice = int(input('Choose time (1 - day//2 - night): '))
    print_all_entities(Weather)
    weather_choice = int(input('Choose weather: '))

    fitting_encounters = read_random_encounter(loc_id=loc_choice, time_id=time_choice, weather_id=weather_choice)
    enc_choice = choice(fitting_encounters)

    while True:
        print(enc_choice)
        user_choice = input('Do you want this encounter? (y - yes//n - next //r - return to menu): ')
        if user_choice == 'y':
            update_entity(Encounter, enc_choice.id, {'done': True})
            print('Encounter is used than successfully!')
            break

        elif user_choice == 'n':
            try:
                fitting_encounters.remove(enc_choice)
                enc_choice = choice(fitting_encounters)
                print()
            except IndexError:
                print(f'\nThese were all the encounters for your options'
                      f'\nLast Encounter: {enc_choice}')
                user_choice = input('Do you want this last encounter? (y - yes//r - return to menu): ')

                if user_choice == 'y':
                    update_entity(Encounter, enc_choice.id, {'done': True})
                    print('Encounter is used than successfully!')
                    break
                elif user_choice == 'r':
                    print('Returning to main menu\n')
                    break
                else:
                    print('Invalid input. Returning to main menu')
                    break

        elif user_choice == 'r':
            print('Returning to main menu\n')
            break

        else:
            print('Invalid input. Please, try again')


encounter_dict = {
    1: print_all_entities,
    2: create_encounter_menu,
    5: delete_all_encounter_menu
}
