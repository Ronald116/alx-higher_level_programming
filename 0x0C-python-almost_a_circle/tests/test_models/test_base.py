#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect

'''
    Create test cases for the base class module
'''


class test_base(unittest.TestCase):
    '''
        Teste base
    '''
    def test_id_none(self):
        '''
            no id
        '''
        b = Base()
        self.assertEqual(5, b.id)

    def test_id(self):
        '''
            valid id
        '''
        b = Base(5)
        self.assertEqual(5, b.id)

    def test_id_zero(self):
        '''
            id 0
        '''
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        '''
            negative id
        '''
        b = Base(-5)
        self.assertEqual(-5, b.id)

    def test_id_string(self):
        '''
            id not an int-string
        '''
        b = Base("Alx")
        self.assertEqual("Alx", b.id)

    def test_id_list(self):
        '''
            id not an int-list
        '''
        b = Base([5, 10, 15])
        self.assertEqual([5, 10, 15], b.id)

    def test_id_dict(self):
        '''
            id  not an int-dict
        '''
        b = Base({"id": 55})
        self.assertEqual({"id": 55}, b.id)

    def test_id_tuple(self):
        '''
            id not an int- tuple
        '''
        b = Base((5,))
        self.assertEqual((5,), b.id)

    def test_to_json_type(self):
        '''
            the json string
        '''
        sq = Square(5)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(type(json_string), str)

    def test_to_json_value(self):
        '''
            Testing the json string
        '''
        sq = Square(10, 20, 30, 40)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_string),
                         [{"id": 40, "y": 30, "size": 10, "x": 20}])

    def test_to_json_None(self):
        '''
            Testing the json string
        '''
        sq = Square(10, 20, 30, 40)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_Empty(self):
        '''
            Testing the json string
        '''
        sq = Square(10, 20, 30, 40)
        json_dict = sq.to_dictionary()
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")


class TestSquare(unittest.TestCase):
    """
        testing Base class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)
