#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
lib_path = os.path.abspath(sys.argv[0])
lib_path = os.path.dirname(lib_path)
lib_path = os.path.join(lib_path,'../..')
sys.path.append(lib_path)

from SQuiXL.DBControllers.PostgresController import PostgresController
from SQuiXL.DBControllers.SQLiteController import SQLiteController
from SQuiXL.Configuration import Loaders

def Example1():
    # Example 1 (With parameters)
    postgres = PostgresController(db_host='localhost', db_user='gear_user', db_password='Africa21', db_port=5432, db_name='gear_db')
    postgres.connect()
    postgres.close()

def Example2():
    # Example 2 (Loading credentials from JSON)
    config = Loaders.loadJSON('config.json')
    postgres = PostgresController(json=config['postgres_credentials'])
    postgres.connect()
    postgres.close()

def Example3():
    # Example 3 (Loading credentials from Database)

        #------------> SHOW tables_credentials.sql <---------------
        # The best option is use two tables: Options(id, name) and Options_values(options_id, key, value)
        # And you can use a view: view_options(options_id, options_name, key, value)

    # You get anyone list of duples (key, value) and convert fetch in json options 
    sqlite = SQLiteController("credentials.db")
    sqlite.connect()
    fetch_credentials = sqlite.select(columns="key,value", table="view_options", where="options_name = \"CREDENTIALS_POSTGRES\"")
    config = Loaders.fetchoptions2JSON(fetch_credentials)
    sqlite.close()

    # Same Example 2 with json
    postgres = PostgresController(json=config)
    postgres.connect()
    postgres.close()

Example1()	