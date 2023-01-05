#!/usr/bin/python3
"""test for console"""

import unittest
from unittest.mock import patch
from io import StringIO
import os
from os import getenv

from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """this will test the console"""

    @classmethod
    def setUpClass(cls):
        """setup for the test"""
        cls.consol = HBNBCommand()

    def setUp(self):
        """Sets up test cases."""
        if os.path.isfile("file.json"):
            os.remove("file.json")
        self.resetStorage()

    def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_emptyline(self):
        """Test empty line input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("\n")
            self.assertEqual('', f.getvalue())

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "can't run if storage is db")
    def test_create(self):
        """Test create command input"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create")
            self.assertEqual(
                "** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create asdfsfsd")
            self.assertEqual(
                "** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:

            self.consol.onecmd("all User")
            self.assertEqual("[User]", f.getvalue()[:7])

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") == "db",
                     "can't run if storage is db")
    def test_create_v2(self):
        """Test create command with parameters."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create State name="California"')
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show State {}".format(id))
            self.assertTrue("'name': 'California'" in f.getvalue())
            self.assertEqual("[State]", f.getvalue()[:7])

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol\
                       .onecmd('create City name="San_Francisco state_id="{}"'
                               .format(id))
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create Place latitude=7.89')
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)

        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show Place {}".format(id))
            self.assertTrue("'latitude': 7.89" in f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create Place max_guest=5')
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show Place {}".format(id))
            self.assertTrue("'max_guest': 5" in f.getvalue())

    def test_create_v2_params(self):
        """Test create command with several parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd('create User email="ilovetim@google.com"\
                               password="timisboss"\
                               first_name="Farrukh" last_name')
            id = f.getvalue()[:-1]
            self.assertEqual(len(id), 36)
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("show User {}".format(id))
            print(f.getvalue())
            self.assertTrue("'email': 'ilovetim@google.com'" in f.getvalue())
            self.assertTrue("'password': 'timisboss'" in f.getvalue())
            self.assertTrue("'first_name': 'Farrukh'" in f.getvalue())

    def test_all(self):
        """Test all command inpout"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all asdfsdfsd")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            self.consol.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())


if __name__ == "__main__":
    unittest.main()
