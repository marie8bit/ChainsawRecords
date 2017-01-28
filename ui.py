import records, choiceProcessor, dbManager
def main():
    dbManager.setup()
    quit = 'q'
    choice = None
    while choice != quit:
        choice = display_menu_get_choice()
        choiceProcessor.handle_choice(choice)


def display_menu_get_choice():

    '''Display choices for user, return users' selection'''

    print('''
        1. Show records
        2. Add a new record
        3. Update a record
        4. Delete a record
        q. Quit
    ''')

    choice = input('Enter your selection: ')

    return choice

def getPositiveInt(string):
    nString = string
    while True:
        try:
            id = int(nString)
            if id >= 0:
                return id
            else:
                print('Please enter a positive number ')
                nstring = input()

        except ValueError:
            print('Please enter an integer number')
            nstring = input()
def getUpdateChoice():
    print('''
        Choose a record to update
    ''')
    choiceProcessor.showAll()
    print('Enter the name of the record holder ')
    print('whose catch record has changed: ')
    choice = input()
    present = dbManager.getRecord(choice)
    if (present == True):
        dbManager.updateRec(choice)

if __name__ == '__main__':
    main()
