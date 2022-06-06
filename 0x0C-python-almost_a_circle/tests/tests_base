#!/usr/bin/python3
"""test file for base modulle"""
import unittest
from models.base import Base


class test_case(unittest.TestCase):
    
    def test1(self):
        b = Base(48)
        self.assertEqual(b.id, 48)

        b = Base()
        self.assertEqual(b.id, 1)

        b = Base()
        self.assertEqual(b.id, 2)

        b = Base()
        self.assertEqual(b.id, 3)

        b = Base("hey")
        self.assertEqual(b.id, "hey")

        self.assertTrue(len(Base.__doc__) > 0)
