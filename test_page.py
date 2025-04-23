# test_page.py
import unittest

class TestHolaMundo(unittest.TestCase):
    def test_content(self):
        with open("index.html", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("<h1>Hola Mundo</h1>", content)

if __name__ == "__main__":
    unittest.main()
