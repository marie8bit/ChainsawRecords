import ui, dbManager
import sqlite3
db = sqlite3.connect('chainsawRecordsDB.db')
cur = db.cursor()
def handle_choice(choice):
    if choice == '1':
        showAll()
    if choice == '2':
        addRecord()
    if choice == '3':
        updateRecord()
    if choice == '4':
        deleteRecord()
    if choice == 'q':
        quit()

def showAll():
    cur.execute('select * from records')
    for row in cur:
        print (row)

def addRecord():
    name = input('Enter Name of Record Holder: ')
    country = input('Enter Country of Record Holder: ')
    stringCatches = input('Enter the recorded number of catches')
    catches = ui.getPositiveInt(stringCatches)
    dbManager.addNewRecord(name, country, catches)

def updateRecord():
    ui.getUpdateChoice()
