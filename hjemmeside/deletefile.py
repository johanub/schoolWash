from sqlite3 import connect
import os

db = connect('{}/db.sqlite3'.format(os.getcwd()))

curser = db.cursor()

def clear():
	curser.execute("delete from frontpage_taken")
	curser.execute("delete from frontpage_tables")
	db.commit()

clear()