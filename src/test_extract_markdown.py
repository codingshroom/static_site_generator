import unittest
from splitters import extract_markdown_links, extract_markdown_images


class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_em_images_empty(self):
        matches = extract_markdown_images("blablabla")
        self.assertListEqual([], matches)
    
    def test_em_images_multi(self):
        matches = extract_markdown_images("blabla![image](https://i.imgur.com/zjjcJKZ.png) more ![image](https://wiki.com/logo.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image", "https://wiki.com/logo.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("blabla[link](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("link", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_em_links_empty(self):
        matches = extract_markdown_links("blablabla")
        self.assertListEqual([], matches)
    
    def test_em_links_multi(self):
        matches = extract_markdown_links("blabla [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)



if __name__ == "__main__":
    unittest.main()
