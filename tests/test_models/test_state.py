#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

class TestDatabaseChanges(unittest.TestCase):
    def setUp(self):
        # Prepare the test environment (e.g., set up database fixtures)

    def tearDown(self):
        # Clean up after the test (e.g., remove temporary data)

    def test_create_state(self):
        # Get the initial count of records
        initial_count = self.get_state_count()

        # Execute the console command to create a state (simulating user interaction)
        # You can use subprocess or similar method to run console commands

        # Get the count of records after the command is executed
        final_count = self.get_state_count()

        # Validate the change in count
        self.assertEqual(final_count, initial_count + 1)
    
    def get_state_count(self):
        # Implement a method to retrieve the count of records from the states table

