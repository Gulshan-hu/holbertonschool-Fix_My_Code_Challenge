#!/usr/bin/env python3
"""
User class
"""

class User():
    """ User class """

    def __init__(self):
        """ Constructor """
        self._password = None

    @property
    def password(self):
        """ Getter for password """
        return self._password

    @password.setter
    def password(self, value):
        """ Setter for password """
        self._password = value

    def is_valid_password(self, password):
        """ Check if password is valid """
        return self._password == password
