"""
@package utils

Util class implementation
All most commonly used utils should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import time
import traceback
import random, string
import utils.custom_logger as cl
import logging

class Util(object):

    log = cl.custom_logger(logging.INFO)

    def get_alpha_numeric(self, length, type='letters'):
        """
        Get random string of characters

        Parameters:
            length: Length of string, number of characters string should have
            type: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types
        """
        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))


    # another wrapper method of getAlphaNumeric
    def get_unique_name(self, char_count=10):
        """
        Get a unique name
        """
        return self.get_alpha_numeric(char_count, 'lower')


    # another wrapper method of getAlphaNumeric
    def get_unique_name_list(self, list=5, item_length=None):
        """
        Get a list of valid email ids

        Parameters:
            list: Number of names. Default is 5 names in a list
            item_length: It should be a list containing number of items equal to the listSize
                        This determines the length of the each item in the list -> [1, 2, 3, 4, 5]
        """
        name_list = []
        for i in range(0, list):
            name_list.append(self.get_unique_name(item_length[i]))
        return name_list


