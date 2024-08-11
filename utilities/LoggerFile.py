import logging
import inspect

class LogGenerator:
    @staticmethod
    def loggen():
        name=inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler(".\\Logs\\OrangeHRMLog.log")
        #search log format in python and copy the format
        logformat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)d : %(message)s")
        logfile.setFormatter(logformat)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger

    #getlogger - captures the log
    #logfile - file where the log is saved
    #logformat - template of the log
    #setformatter - link file and format
    #addhandler - maintain logs everytime in log file

    #debug, info, warnings, error, critical - Log Levels

