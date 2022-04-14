#!/usr/bin/python3
""" Unittest of Base class"""

import unittest
from datetime import datetime
import time
from models.user import User


class TestUser(unittest.TestCase):
    """ Test of class User """

    def test_id(self):
        """test for id attribute of User
        """
        u = User()
        self.assertEqual(type(u.id), type("a"))

    def test_email(self):
        """test for email attribute of User
        """
        u = User(email="a@gmail.com")
        self.assertEqual(u.email, "a@gmail.com")

    def test_password(self):
        """test for password attribute of User
        """
        u = User(password="aaaaa")
        self.assertEqual(u.password, "aaaaa")

    def test_first_name(self):
        """test for first name attribute of User
        """
        u = User(first_name="test")
        self.assertEqual(u.first_name, "test")

    def test_last_name(self):
        """test for last name attribute of User
        """
        u = User(last_name="test")
        self.assertEqual(u.last_name, "test")

    def test_to_dict(self):
        """test for method to_dict of User
        """
        u = User(email="a")
        udic = u.to_dict()
        self.assertEqual(udic['email'], "a")

    def test_str(self):
        """test for method __str__ of User
        """
        u = User()
        self.assertEqual(str(u)[0:6], "[User]")

    def test_init_kwargs(self):
        """test for method __init__ of User by kwagrs
        """
        u = User()
        udic = u.to_dict()
        c = User(**udic)
        self.assertEqual(u.id, c.id)

    def test_init_kwargs2(self):
        """test for method __init__ of User by kwagrs
        """
        u = User(email="a")
        udic = u.to_dict()
        c = User(**udic)
        self.assertEqual(u.email, c.email)


if __name__ == "__main__":
    unittest.main()
