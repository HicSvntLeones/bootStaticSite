import unittest

from html_leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_noProps(self):
        node = LeafNode("tag", "value")
        self.assertIsNone(node.props)

    def test_hasValues(self):
        node = LeafNode("tag", "value", "props")
        self.assertEqual(node.tag, "tag")
        self.assertEqual(node.value, "value")
        self.assertEqual(node.props, "props")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")
    
    def test_leaf_to_html_b(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()