#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

class Logging:

    log_format='%(asctime)s %(levelname)-8s %(message)s'
    log_time_format='%y%m%d-%H:%M:%S'

    def __init__(self, mode=logging.INFO):

        self.mode_log = mode

        logging.basicConfig(level=self.mode_log, format=self.log_format, datefmt=self.log_time_format)

        # if self.log_in_file:
        #     self.errorLog = os.path.join(self.dir_errorLog, self.file_errorLog)
        #     file_handler = logging.FileHandler(filename=self.errorLog, mode='a')
        #     file_handler.setFormatter(logging.Formatter(self.log_format))
        #     file_handler.setLevel(self.mode_log)
        #     logger = logging.getLogger('')
        #     logger.addHandler(file_handler)

        logging.info("Initializing Log System")

    # Metodos de impresion por pantalla de logs.
    def info(self, texto):
        logging.info(texto)

    def debug(self, texto):
        logging.debug(texto)
    
    def warning(self, texto):
        logging.warning(texto)
    
    def error(self, texto):
        logging.error(texto)