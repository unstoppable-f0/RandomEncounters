from db.sql_queries import (
add_location
)

location_dict = {1: 'bubba'}

def main():
    # 1 - get an encounter

    # 2 - make new encounter
        # -- creation process --

    # 3 - work with encounters
        # 1 -- get all
        # 2 -- change
        # 3 -- delete
        # 4 -- delete all
        # 5 -- back

    # 4 - work with locations
        # 1 -- get all
        # 2 -- change
        # 3 -- delete
        # 4 -- delete all
        # 5 -- back

    # 5 - work with weather
        # 1 -- get all
        # 2 -- change
        # 3 -- delete
        # 4 -- delete all
        # 5 -- back

    # 6 - exit
    pass

if __name__ == '__main__':
    while True:
        print('Welcome to the Random Encounters! What do you want to do?')
        print('1. Add Location')
        print('2. Exit')

        choice = input('Enter your choice: ')
        if choice == '1':
            add_location(input('Name your Location: '))
        elif choice == '2':
            print('Goodbye!')
            break
