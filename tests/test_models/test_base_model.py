#!/usr/bin/python3
"""
BaseModel unittests
"""
import os
import unittest
import pep8
from models.base_model import BaseModel


class BaseModel_test(unittest.TestCase):
    """ testing BaseModel """

    @classmethod
    def setUp(cls):
        """ New BaseModel  """
        cls.new_model = BaseModel()

    def test_save(self):
        """ test for save"""
        self.insta.save()
        self.assertNotEqual(self.insta.created_at, self.insta.updated_at)
        elf.an = self.insta.updated_at
        self.insta.save()
        self.des = self.insta.updated_at
        self.assertIsNot(self.an, self.des)

    def test_created_at_fun_test(self):
        """ create functionality"""
        self.assertEqual(datetime, type(self.insta.created_at))

    def test_updated_at_fun_test(self):
        """ updated functionality"""
        self.assertEqual(datetime, type(self.insta.updated_at))

    @classmethod
    def tearDown(cls):
        """ Delete  """
        del cls.new_model
        try:
            os.remove('file.json')
        except BaseException:
            pass

   def test_dictionary_test(self):
        '''dictionary method'''
        test_dict = self.insta.to_dict()
        self.assertEqual(type(test_dict), dict)
        self.assertTrue('to_dict' in dir(self.insta))
        self.assertIsInstance(test_dict["created_at"], str)
        self.assertIsInstance(test_dict["updated_at"], str)

    def test_pep8(self):
            """ pep8 testing """
            p8 = pep8.StyleGuide(quiet=True)
            asw = p8.check_files(['models/base_model.py'])
            self.assertEqual(asw.total_errors, 0, "Fix Style")


if __name__ == "__main__":
    unittest.main()
