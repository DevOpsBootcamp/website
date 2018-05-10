#!/usr/bin/python
import MySQLdb
import os

db = MySQLdb.connect(
  os.environ['MYSQL_PORT_3306_TCP_ADDR'],
  'root',
  os.environ['MYSQL_ENV_MYSQL_ROOT_PASSWORD'],
  "nobel"
)

cursor = db.cursor()
cursor.execute("SELECT subject, yr, winner FROM nobel WHERE yr = 1960")
data = cursor.fetchall()

for winner in data:
    print "%s winner in %s: %s " % (winner[0], winner[1], winner[2])

db.close()
