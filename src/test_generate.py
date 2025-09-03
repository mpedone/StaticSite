import unittest
from generate import extract_title

class test_generate(unittest.TestCase):
    def test_one(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title, "Hello")
    
    def test_two(self):
        with self.assertRaises(Exception):
            extract_title("## Hello")
        with self.assertRaises(Exception):
            extract_title("### Hello")
        with self.assertRaises(Exception):
            extract_title("#### Hello")
        with self.assertRaises(Exception):
            extract_title("##### Hello")
        with self.assertRaises(Exception):
            extract_title("###### Hello")
        with self.assertRaises(Exception):
            extract_title(" Hello")
        with self.assertRaises(Exception):
            extract_title("Hello")
        with self.assertRaises(Exception):
            extract_title("")
        with self.assertRaises(Exception):
            extract_title("> quote")
        with self.assertRaises(Exception):
            extract_title("```code ```")
        with self.assertRaises(Exception):
            extract_title("- ul\n- ul2")
        with self.assertRaises(Exception):
            extract_title("#1 hello")
        with self.assertRaises(Exception):
            extract_title(" # hello")
    
    def test_three(self):
        self.assertEqual(extract_title("# "), "")
    
    def test_four(self):
        self.assertEqual(extract_title("# #title"), "#title")

if __name__ == "__main__":
    unittest.main()