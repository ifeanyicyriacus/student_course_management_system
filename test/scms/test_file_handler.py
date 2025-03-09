import os
import unittest
import uuid

from src.scms.file_handler import FileHandler

class TestFileHandlerFunctions(unittest.TestCase):

    def setUp(self):
        random_file_name = str(uuid.uuid4())
        self.file_path = f"./../data/test/{random_file_name}.txt"
        self.file_handler = FileHandler(self.file_path)

    def tearDown(self):
        os.remove(self.file_path)

    def test_write_function_writes_a_line_to_file(self):
        self.file_handler.write("hello world")
        expected = ["hello world"]
        actual = self.file_handler.read()
        self.assertEqual(expected, actual)

    def test_read_function_can_write_multiple_line_to_file(self):
        self.file_handler.write("hello world")
        self.file_handler.write("how are you")
        self.file_handler.write("goodbye")
        actual = self.file_handler.read()
        expected = ["hello world", "how are you", "goodbye"]
        self.assertEqual(expected, actual)

    def test_read_function_can_write_to_file_when_file_does_not_exist(self):
        self.file_handler.write("hello world")
        expected = ["hello world"]
        actual = self.file_handler.read()
        self.assertEqual(expected, actual)

    def test_read_function_can_read_from_file_when_file_does_not_exist(self):
        actual = self.file_handler.read()
        expected = []
        self.assertEqual(expected, actual)