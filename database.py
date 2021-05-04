import sqlite3

def ensureConnection(func):
	def inner(*args, **kwargs):
		with sqlite3.connect("database.db") as conn:
			kwargs["conn"] = conn
			res = func(*args, **kwargs)
		return res
	return inner

@ensureConnection
def initDB(conn, force: bool = False):
	c = conn.cursor()
	if force:
		c.execute("DROP TABLE IF EXISTS userRequests")
		c.execute("DROP TABLE IF EXISTS userList")
	c.execute("""
		CREATE TABLE IF NOT EXISTS userRequests (
			userID          INTEGER NOT NULL,
			horizontalAxis  TEXT NOT NULL,
			verticalAxis    TEXT NOT NULL,
			timeNow         TEXT NOT NULL,
			dayNow          TEXT NOT NULL
		)
	""")
	c.execute("""
		CREATE TABLE IF NOT EXISTS userList (
			userID          INTEGER PRIMARY KEY,
			timeNow         TEXT NOT NULL,
			dayNow          TEXT NOT NULL
		)
	""")
	conn.commit()

@ensureConnection
def saveRequest(conn, userID: int, horizontalAxis: int, verticalAxis: int,  timeNow: str, dayNow: str):
	c = conn.cursor()
	c.execute("INSERT INTO userRequests (userID, horizontalAxis, verticalAxis, timeNow, dayNow) VALUES (?, ?, ?, ?, ?)", (userID, horizontalAxis, verticalAxis, timeNow, dayNow))
	conn.commit()

@ensureConnection
def userList(conn, userID: int, timeNow: str, dayNow: str):
	c = conn.cursor()
	c.execute("INSERT OR IGNORE INTO userList (userID, timeNow, dayNow) VALUES (?, ?, ?)", (userID, timeNow, dayNow))
	conn.commit()