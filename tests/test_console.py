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
