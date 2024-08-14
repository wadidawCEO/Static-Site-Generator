import unittest

from block import markdown_to_blocks


class TestBlock(unittest.TestCase):
    def test_block(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        splitted_blocks = markdown_to_blocks(markdown)
        expected_output = [
                        '# This is a heading', 
                        'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                        '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        self.assertEqual(splitted_blocks, expected_output)

    def test_block_single(self):
        markdown = """# This is a heading"""
        splitted_blocks = markdown_to_blocks(markdown)
        expected_output = [
                        '# This is a heading', 
        ]
        self.assertEqual(splitted_blocks, expected_output)

    def test_block_extra_whitespace(self):
        markdown = """# This is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.

                * This is the first list item in a list block
                * This is a list item
                * This is another list item"""
        splitted_blocks = markdown_to_blocks(markdown)
        expected_output = [
                        '# This is a heading', 
                        'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                        '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        self.assertEqual(splitted_blocks, expected_output)

    def test_block_extra_ending_whitespace(self):
        markdown = """# This is a heading

                This is a paragraph of text. It has some **bold** and *italic* words inside of it.   

                * This is the first list item in a list block  
                * This is a list item  
                * This is another list item           """
        splitted_blocks = markdown_to_blocks(markdown)
        expected_output = [
                        '# This is a heading', 
                        'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', 
                        '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        self.assertEqual(splitted_blocks, expected_output)

    def test_block_leading_whitespace(self):
        markdown = """# This is a heading


            This is a paragraph with leading whitespace.

        * An unordered list item
        * Another list item"""
        splitted_blocks = markdown_to_blocks(markdown)
        expected_output = [
            '# This is a heading', 
            'This is a paragraph with leading whitespace.', 
            '* An unordered list item\n* Another list item'
        ]
        self.assertEqual(splitted_blocks, expected_output)

    def test_block_empty(self):
        markdown = """"""
        splitted_blocks = markdown_to_blocks(markdown)
        expected_output = []
        self.assertEqual(splitted_blocks, expected_output)

    def test_block_just_spaces(self):
        markdown = "  "
        splitted_blocks = markdown_to_blocks(markdown)
        expected_output = []
        self.assertEqual(splitted_blocks, expected_output)

if __name__ == "__main__":
    unittest.main()