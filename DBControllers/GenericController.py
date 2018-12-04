#!usr/bin/env Python
# -*- coding: utf-8 -*-

from SQuiXL.Configuration.Logging import Logging

class GenericController:

    logging = Logging()

    def close(self):
        self.connection.close()
        self.logging.info("Closed connection to DB")

    def select(self, columns='*', table='dual', where=None):
        cursor = self.connection.cursor()
        sql = "SELECT {} FROM {}".format(columns,table)
        if where is not None:
            sql += " WHERE {}".format(where)
        self.logging.debug("The Select that will be executed".format(sql))
        cursor.execute(sql)
        return cursor.fetchall()