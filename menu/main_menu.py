from menu.weather_menu import weather_menu
from menu.location_menu import location_menu
from menu.encounter_menu import encounter_menu, read_random_enc_menu


def main_menu() -> None:
    """Main menu function"""

    while True:
        print("Welcome to the Main Menu. Choose an option: "
              "\n1. Get an encounter"
              "\n2. Encounters"
              "\n3. Locations"
              "\n4. Weather"
              "\n5. Exit\n")

        try:
            user_choice = int(input("Enter your choice: "))
            if user_choice == 5:
                break
            else:
                main_menu_dict[user_choice]()
        except (ValueError, KeyError):
            print("Invalid input. Please try again.\n")


# ### menu dicts ###

main_menu_dict = {
    1: read_random_enc_menu,
    2: encounter_menu,
    3: location_menu,
    4: weather_menu,
}

if __name__ == '__main__':
    main_menu()
