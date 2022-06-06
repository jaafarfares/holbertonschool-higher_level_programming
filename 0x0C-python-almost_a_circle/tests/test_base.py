#!/usr/bin/python3
"""test file for base modulle"""
import unittest
from models.base import Base


class test_case(unittest.TestCase):
    
    def test1(self):
        b = Base(48)
        self.assertEqual(b.id, 48)
