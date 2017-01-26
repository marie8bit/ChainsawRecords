import sqlite3
import traceback
db = sqlite3.connect('chainsawRecordsDB.db')
cur = db.cursor()
def setup():
    try:

        cur.execute('create table if not exists records (name text, country text, catches int)')
        cur.execute('select * from records')
        data = cur.fetchall()
        if (len(data)==0):
            cur.execute('insert into records values ("Ian Stewart", "Canada", 94)')
            cur.execute('insert into records values ("Aaron Gregg", "Canada", 88)')
            cur.execute('insert into records values ("Chad Taylor", "USA", 78)')
            cur.execute('select * from records')
            for row in cur:
                print (row)
                db.commit()
        else:
            for row in cur:
                print (row)
    except sqlite3.Error as e:
        print('rolling back changes because of error:', e)
        traceback.print_exc()
        db.rollback()
    # finally:
    #     print('closing database')
    #     db.close()
def addNewRecord(name, country, catches):
    cur.execute('insert into records values (?, ?, ?)', (name, country, catches))
    db.commit()
    print('New record added to database')

def getRecord(name):
    data = cur.execute('select * from records where name = ?', (name))
    if (len(data) !=0):
        updateRec(name)
    else:
        print('Record not found, please try again')

def updateRec(name):
    print ('Enter the new number of catches for '+name)
    stringCa= input()
    catc = getPositiveInt(stringCa)
    cur.execute('update records set catches = ? where name = ?', (catc, name))
    cur.commit()
    print
