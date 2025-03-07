import unittest
import uuid

from src.scms.file_handler import FileHandler

class TestFileHandlerFunctions(unittest.TestCase):

    def test_write_function_writes_a_line_to_file(self):
        FileHandler.write("resources/hello1.txt", "hello world")
        expected = ["hello world"]
        actual = FileHandler.read("resources/hello1.txt")
        self.assertEqual(expected, actual)

    def test_read_function_can_write_multiple_line_to_file(self):
        FileHandler.write("resources/hello.txt", "hello world")
        FileHandler.write("resources/hello.txt", "how are you")
        FileHandler.write("resources/hello.txt", "goodbye")
        actual = FileHandler.read("resources/hello.txt")
        expected = ["hello world", "how are you", "goodbye"]
        self.assertEqual(expected, actual)

    def test_read_function_can_write_to_file_when_file_does_not_exist(self):
        random_file_name = str(uuid.uuid4())
        FileHandler.write(f"resources/{random_file_name}.txt", "hello world")
        expected = ["hello world"]
        actual = FileHandler.read(f"resources/{random_file_name}.txt")
        self.assertEqual(expected, actual)

    def test_read_function_can_read_from_file_when_file_does_not_exist(self):
        random_file_name = str(uuid.uuid4())
        actual = FileHandler.read(f"resources/{random_file_name}.txt")
        expected = []
        self.assertEqual(expected, actual)