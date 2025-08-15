import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_only_title(self):
        md = "# hello"
        extracted = extract_title(md)
        self.assertEqual(extracted, "hello")

    def test_text_and_title(self):
        md = """
# scenius

we are here to celebrate
joyfully
"""
        extracted = extract_title(md)
        self.assertEqual(extracted, "scenius")

    def test_other_headers(self):
        md = """
# we are 

## well played

### joyfully
"""
        extracted = extract_title(md)
        self.assertEqual(extracted, "we are")


    def test_header_at_end(self):
        md = """
## well played

### joyfully

# _italic_
"""
        extracted = extract_title(md)
        self.assertEqual(extracted, "_italic_")


    def test_no_header(self):
        md = """
## well played

### joyfully
more text
"""
        with self.assertRaises(Exception):
            extract_title(md)


    def test_no_header_2(self):
        md = """
#well played 

### joyfully
more text
"""
        with self.assertRaises(Exception):
            extract_title(md)




if __name__ == "__main__":
    unittest.main()
