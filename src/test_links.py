import unittest

from extract_links import extract_markdown_images, extract_markdown_links

class test_extract_funcs(unittest.TestCase):
    def test_one(self):
        matches = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
    
    def test_no_alt_text(self):
        matches = extract_markdown_images("This is bad markdown, just look at how grumpy grumpy cat is: (https://notarealcat.gif)")
        self.assertEqual([], matches)
    
    def test_no_image(self):
        matches = extract_markdown_images("Blah blah blah ![blah]")
        self.assertEqual([], matches)
    
    def test_http(self):
        matches = extract_markdown_images("This is text with a ![rick roll](http://i.imgur.com/aKaOqIh.gif) and ![obi wan](http://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertEqual([("rick roll", "http://i.imgur.com/aKaOqIh.gif"), ("obi wan", "http://i.imgur.com/fJRm4Vk.jpeg")], matches)

    def test_http_link(self):
        matches = extract_markdown_links("This is a non-secure [website](http://gimme.com)")
        self.assertEqual([("website", "http://gimme.com")], matches)
    
    def test_non_standard(self):
        matches = extract_markdown_links("[file transfer](ftp://hereyougo.com) and [just the domain](sketchy.com)")
        self.assertEqual([("file transfer", "ftp://hereyougo.com"), ("just the domain", "sketchy.com")], matches)

if __name__ == "__main__":
    unittest.main()