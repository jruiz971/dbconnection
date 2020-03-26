#!/usr/bin/env python3
import json
import mysql.connector
from mysql.connector import errorcode

#with open("db.json", "w") as write_file:
#    json.dump(config, write_file)

with open('db.json') as json_file:
    config = json.load(json_file)

try:
    cnx = mysql.connector.connect(**config,auth_plugin='mysql_native_password')
    
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
