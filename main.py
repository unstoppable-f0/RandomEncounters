from db.sql_queries import (
add_location
)

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
