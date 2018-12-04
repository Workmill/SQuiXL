#!usr/bin/env Python
# -*- coding: utf-8 -*-

import psycopg2
from SQuiXL.DBControllers.GenericController import GenericController

class PostgresController(GenericController):

    def __init__(self, db_host='localhost', db_user='postgres', db_password='postgres', db_port=5432, db_name='postgres', json=None):
        self.logging.info("Creating Postgrest Controller")
        if json is None:
            self.db_host = db_host
            self.db_user = db_user
            self.db_password = db_password
            self.db_port = db_port
            self.db_name = db_name
        else:
            self.db_host = json['db_host']
            self.db_user = json['db_user']
            self.db_password = json['db_password']
            self.db_port = json['db_port']
            self.db_name = json['db_name']


    def connect(self):
        try:
            self.connection = psycopg2.connect(host=self.db_host,
                                          user=self.db_user,
                                          password=self.db_password,
                                          port=self.db_port,
                                          dbname=self.db_name)
            self.logging.info("Connected to Posgres")
        except Exception as e:
            self.logging.error("Cannot connect to Databsse: {}".format(e))
            exit(1)