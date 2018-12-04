#!usr/bin/env Python
# -*- coding: utf-8 -*-

import sqlite3
from SQuiXL.DBControllers.GenericController import GenericController

class SQLiteController(GenericController):

    def __init__(self, file):
        self.file = file

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.file)
            self.logging.info("Creating SQLite Controller")
        except Exception as e:
            self.logging.error("Cannot connect to Posgres: {}".format(e))
            exit(1)
