from db.sql_queries import get_all_weather


def print_all_weather():
    """Print all locations"""

    for weather in get_all_weather():
        print(f'{weather.id}. {weather.name}')
    print("\n")


def get_all_weather_ids_and_print() -> list[int]:
    """Get all ids of locations and print them in a proper manner."""

    all_weather = get_all_weather()
    all_weather_ids = [weather.id for weather in all_weather]

    for weather in all_weather:
        print(f'{weather.id}. {weather.name}')
    print('\n')

    return all_weather_ids
