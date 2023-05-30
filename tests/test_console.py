#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import DogPlug

class TestDogPlug(unittest.TestCase):

    def setUp(self):
        self.console = DogPlug()

    def test_complete_greet(self):
        completions = self.console.complete_greet("", "greet ", 0, 6)
        self.assertEqual(completions, ['Tony', 'Maiyo', 'Lupin'])

        completions = self.console.complete_greet("T", "greet T", 0, 7)
        self.assertEqual(completions, ['Tony'])

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_greet(self, mock_stdout):
        self.console.onecmd("help greet")
        expected_output = "greet [person]\nGreet the named person"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        self.assertFalse(self.console.emptyline())
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_do_quit(self):
        self.assertTrue(self.console.onecmd("quit"))

    def test_do_EOF(self):
        self.assertTrue(self.console.onecmd("EOF"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_create(self, mock_stdout):
        self.console.onecmd("help create")
        expected_output = "Create class instance\nUsage: create <class name>"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_complete_create(self):
        completions = self.console.complete_create("", "create ", 0, 7)
        self.assertEqual(completions, self.console.classes)

        completions = self.console.complete_create("B", "create B", 0, 8)
        self.assertEqual(completions, ['BaseModel'])
    
    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        # Test create command
        self.console.onecmd("create Dog name='Buddy' age=3 weight=10.5")
        instance_id = mock_stdout.getvalue().strip()
        self.assertTrue(instance_id)

        # Check if the created instance is stored
        self.assertIn(f"Dog.{instance_id}", self.console.storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_invalid_class(self, mock_stdout):
        # Test create command with invalid class name
        self.console.onecmd("create InvalidClass")
        expected_output = "**Invalid class name**"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create_missing_class_name(self, mock_stdout):
        # Test create command with missing class name
        self.console.onecmd("create")
        expected_output = "**class name missing**"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_do_create_invalid_params(self):
        # Test create command with invalid parameters
        self.console.onecmd("create Dog name='Buddy' age='invalid' weight=10.5")
        self.assertNotIn("Dog.", self.console.storage.all())


    @patch('sys.stdout', new_callable=StringIO)
    def test_help_show(self, mock_stdout):
        # Test help_show method
        self.console.onecmd("help show")
        expected_output = "Show attributes of a specific class instance\nUsage: destroy <class name> <instance id>"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_complete_show(self):
        # Test complete_show method
        completions = self.console.complete_show("", "show ", 0, 5)
        self.assertEqual(completions, self.console.classes)

        completions = self.console.complete_show("B", "show B", 0, 6)
        self.assertEqual(completions, ['BaseModel'])
    


if __name__ == '__main__':
    unittest.main()
