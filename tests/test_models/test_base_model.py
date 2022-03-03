#!/usr/bin/python3
""" Unittest of Base class"""

import unittest
from datetime import datetime
import time
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """ Test of class Base """

    def test_id(self):
        """test for id attribute of BaseModel
        """
        b = BaseModel()
        self.assertEqual(type(b.id), type("abc"))

    def test_created_at(self):
        """test for created_at attribute of base
        """
        b = BaseModel()
        d = datetime.now()
        self.assertEqual(str(b.created_at)[0:-10], d.strftime('%Y-%m-%d %H:%M'))

    def test_updated_at(self):
        """test for updated_at attribute of base
        """
        b = BaseModel()
        d = datetime.now()
        self.assertEqual(str(b.updated_at)[0:-10], d.strftime('%Y-%m-%d %H:%M'))

    def test_name(self):
        """test for name attribute of base
        """
        b = BaseModel()
        b.name = "test"
        self.assertEqual(b.name, "test")

    def test_name2(self):
        """test for name attribute of base
        """
        b = BaseModel()
        b.name = None
        self.assertEqual(b.name, None)

    def test_name3(self):
        """test for name attribute of base
        """
        b = BaseModel()
        b.name = ""
        self.assertEqual(b.name, "")

    def test_name4(self):
        """test for name attribute of base
        """
        b = BaseModel(name="b")
        self.assertEqual(b.name, "b")

    def test_my_number(self):
        """test for my_number attribute of base
        """
        b = BaseModel()
        b.my_number = 1
        self.assertEqual(b.my_number, 1)

    def test_my_number2(self):
        """test for my_number attribute of base
        """
        b = BaseModel(my_number=None)
        self.assertEqual(b.my_number, None)

    """def test_method_save(self):
        b = BaseModel()
        time.sleep(60)
        b.save()
        up = b.updated_at
        d = datetime.now()
        self.assertEqual(str(up)[0:-10], d.strftime('%Y-%m-%d %H:%M'))
    *** il faut trop de temps a lancer donc decommentaire a la fin
    """

    def test_to_dict(self):
        """test for method to_dict of base
        """
        b = BaseModel()
        bdic = b.to_dict()
        self.assertEqual(b.created_at.isoformat(), bdic['created_at'])

    def test_to_dict2(self):
        """test for method to_dict of base
        """
        b = BaseModel()
        bdic = b.to_dict()
        self.assertEqual(b.updated_at.isoformat(), bdic['updated_at'])

    def test_to_dict3(self):
        """test for method to_dict of base
        """
        b = BaseModel()
        bdic = b.to_dict()
        self.assertEqual(b.id, bdic['id'])

    def test_to_dict4(self):
        """test for method to_dict of base
        """
        b = BaseModel(name="b")
        bdic = b.to_dict()
        self.assertEqual(b.name, bdic['name'])

    def test_to_dict5(self):
        """test for method to_dict of base
        """
        b = BaseModel(my_number=1)
        bdic = b.to_dict()
        self.assertEqual(b.my_number, bdic['my_number'])

if __name__ == "__main__":
    unittest.main()
