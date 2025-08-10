import unittest
from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
        html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
    )

    def test_codeblock(self):
        md = """
        ```
        This is text that _should_ remain
        the **same** even with inline stuff
        ```
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )


    def test_unordered_list(self):
        md = """
        we have here an unordered list:
        - who cares
        - nobody wants to know
        - what else?

        **bold spatz**_with italic_`coded gold`
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>we have here an unordered list:</p><ul><li>who cares</li><li>nobody wants to know</li><li>what else?</li></ul><p>\n<b>bold spatz</b><i>with italic</i><code>coded gold</code></div>",
        )


    def test_ordered_list(self):
        md = """
        **bold spatz**_with italic_`coded gold`
        we have here an ordered list:
        1. who cares
        2. nobody wants to know
        3. what else?

        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>\n<b>bold spatz</b><i>with italic</i><code>coded gold</code><p>we have here an ordered list:</p><ol><li>who cares</li><li>nobody wants to know</li><li>what else?</li></ol></div>",
        )


    def test_ordered_list_2(self):
        md = """
        1. who cares
        2. nobody wants to know
        3. what else?
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>who cares</li><li>nobody wants to know</li><li>what else?</li></ol></div>",
        )


    def test_unordered_list_2(self):
        md = """
        - who cares
        - nobody wants to know
        - what else?
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>who cares</li><li>nobody wants to know</li><li>what else?</li></ul></div>",
        )


    def test_ordered_list_wrong(self):
        md = """
        2. who cares
        2. nobody wants to know
        3. what else?
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>2. who cares\n2. nobody wants to know\n3. what else?</p></div>",
        )


    def test_unordered_list_wrong(self):
        md = """
        - who cares
        -nobody wants to know
        - what else?
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>- who cares\n-nobody wants to know\n- what else?</p></div>",
        )


    def test_headings(self):
        md = """
        # heading1
        
        ## heading2

        ### heading3

        #### heading4

        ##### heading5

        ###### heading6
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>heading1</h1><h2>heading2</h2><h3>heading3</h3><h4>heading4</h4><h5>heading5</h5><h6>heading6</h6></div>",
        )


    def test_quotes(self):
        md = """
        >who cares
        >nobody wants to know
        >what else?
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>who cares\nnobody wants to know\nwhat else?</blockquote></div>",
        )


    def test_special_inline(self):
        md = """
        # heading **with** bold
        
        ## _italic_ heading

        ### head`in`g

        #### `heading`

        ##### **heading**

        ###### _heading_

        1. **bold**
        2. _italic_
        3. `code`

        - **bold**
        - _italic_
        - `code`
        
        >**bold**
        >_italic_
        >`code`
        """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            """
            <div><h1>heading <b>with</b> bold</h1>
            <h2><i>italic</i> heading</h2>
            <h3>head<code>in</code>g</h3>
            <h4><code>heading</code></h4>
            <h5><b>heading</b></h5>
            <h6><i>heading</i></h6></div>
            <ol><li><b>bold</b></li>
            <li><i>italic</i></li>
            <li><code>code</code></li></ol>
            <ul><li><b>bold</b></li>
            <li><i>italic</i></li>
            <li><code>code</code></li></ul>
            <blockquote><b>bold</b>
            <i>italic</i>
            <code>code</code></blockquote>
            """,
        )


if __name__ == "__main__":
    unittest.main()
