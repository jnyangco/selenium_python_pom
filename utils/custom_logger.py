import inspect
import logging

# log options -> debug, info, warn, error, critical


def custom_logger(log_level=logging.DEBUG): # default (if you don't specify upon calling log) -> debug
    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    # file_handler = logging.FileHandler("{0}.log".format(logger_name), mode='w')  # write
    # file_handler = logging.FileHandler("automation.log", mode='a')  # mode='a' -> append, mode='w' -> write
    file_handler = logging.FileHandler("automation.log", mode='a')  # write
    file_handler.setLevel(log_level)

    # name = classname "SeleniumDriver" - remove "- %(name)s" if you want to not print the classname in the log file
    # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
    #                 datefmt='%m/%d/%Y %I:%M:%S %p')

    # log with classname
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

    # log without classname
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
