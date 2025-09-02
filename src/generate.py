import re

def extract_title(markdown):
    header = re.search(r"^# (.*)", markdown)
    if header is None:
        raise Exception("No H1 found.")
    title = header.group(1)
    return title

try:
    print(extract_title("# hello"))
except Exception as e:
    print(e)

import unittest


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
    
    def test_three(self):
        self.assertEqual(extract_title("# "), "")

if __name__ == "__main__":
    unittest.main()