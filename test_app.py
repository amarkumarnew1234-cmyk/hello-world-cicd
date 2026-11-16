import unittest
from app import hello_world, welcome_message


class TestHelloWorld(unittest.TestCase):

    def test_hello_world_message(self):
        self.assertEqual(
            hello_world(),
            "Hello, DevOps!"
        )

    def test_hello_world_return_type(self):
        self.assertIsInstance(
            hello_world(),
            str
        )

    def test_welcome_message_amar(self):
        self.assertEqual(
            welcome_message("Amar"),
            "Welcome to DevOps, Amar!"
        )

    def test_welcome_message_student(self):
        self.assertEqual(
            welcome_message("Student"),
            "Welcome to DevOps, Student!"
        )


if __name__ == "__main__":
    unittest.main()
