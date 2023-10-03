#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ test_state to test the state class """

    def __init__(self, *args, **kwargs):
        """ initialises a test_state object"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ test the name attribute of State """
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_updated_at(self):
        """ Test the updated_at attribute of State """
        state = State()
        state.updated_at = "2023-10-02 14:27:05"
        self.assertEqual(state.updated_at, "2023-10-02 14:27:05")
    
    def test_new_attribute(self):
        """Testing the addition of a new attribute"""
        state = State()
        state.new_attribute = "new value"
        self.assertTrue(hasattr(state, "new_attribute"))
        self.assertEqual(state.new_attribute, "new value")

if __name__ == '__main__':
    unittest.main()
