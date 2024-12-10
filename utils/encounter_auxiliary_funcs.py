from db.tables import Encounter, Location, Weather
from utils.entities_funcs import get_all_entities_ids_and_print


def update_encounter_name(encounter: Encounter) -> None:
    """Update the name of the encounter."""

    encounter.name = input('Enter new encounter name: ')


def update_encounter_link(encounter: Encounter) -> None:
    """Update the link of the encounter."""

    encounter.link = input('Enter new encounter link: ')


def update_encounter_time(encounter: Encounter) -> None:
    """Update the time of the encounter."""

    print('Choose the new time of day:\n'
          'Day - 1\n'
          'Night - 2\n'
          'Both - 3\n'
          '(choose only one!)')

    time_of_day = input('Enter the time: ')
    # time validation
    if len(time_of_day) == 1 and time_of_day in ('1', '2', '3'):
        encounter.time = int(time_of_day)
        print('Got the time\n')
    else:
        print('Wrong input. Going forward')


def update_encounter_location(encounter: Encounter) -> None:
    """Update the locations of the encounter."""

    all_old_locations = encounter.locations
    print(f'Current locations: {", ".join(all_old_locations)}')

    all_locs_ids = get_all_entities_ids_and_print(Location)
    try:
        user_locs = input('Choose id(s) of location(s) of the encounter (separated by space if many): ').split()
        user_locs = list(map(int, user_locs))
    except ValueError:
        print("Invalid input. Locations won't be updated")
        return

    if set(all_locs_ids).issuperset(set(user_locs)) and len(user_locs) >= 1:
        encounter.locations = map(int, user_locs)
        print('Got the locations')
    else:
        print('Wrong input. Going forward')


def update_encounter_weather(encounter: Encounter) -> None:
    """Update the weather conditions of the encounter."""

    all_old_weather = encounter.weather
    print(f'Current locations: {", ".join(all_old_weather)}')

    all_weather_ids = get_all_entities_ids_and_print(Weather)
    try:
        user_weather = input('Choose id(s) of weather of the encounter (separated by space if many): ').split()
        user_weather = list(map(int, user_weather))
    except ValueError:
        print('Invalid input. Returning to main menu')
        return

    if set(all_weather_ids).issuperset(set(user_weather)) and len(user_weather) >= 1:
        encounter.weather = user_weather
        print('Got the weather\n')
    else:
        print('Wrong input. Going forward')


def update_encounter_status(encounter: Encounter) -> None:
    """Update the status of the encounter."""

    print(f'Curren encounter status is {"FINISHED" if encounter.done else "ACTIVE"}')
    user_choice = input('Do you want to change the status of the encounter? (y/n): ')
    if user_choice == 'y':
        encounter.done = not encounter.done
    elif user_choice == 'n':
        print('Returning...')
        return
    else:
        print('Invalid input. Returning to changing the encounter')


def update_encounter_prerequisites(encounter: Encounter) -> None:
    """Update the prerequisites of the encounter."""

    encounter.prerequisites = input('Insert new prerequisites for the encounter: ')


update_encounter_dict = {
    1: update_encounter_name,
    2: update_encounter_link,
    3: update_encounter_time,
    4: update_encounter_location,
    5: update_encounter_weather,
    6: update_encounter_status,
    7: update_encounter_prerequisites
}
