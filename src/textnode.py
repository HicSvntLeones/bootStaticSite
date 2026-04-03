from enum import Enum

class TextType(Enum):
    TEXT = "air"
    BOLD = "water"
    ITALIC = "earth"
    CODE = "fire"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if self.text == other.text & self.text_type == other.text_type & self.url == other.url:
            return True
        return False
    
    def __repr__(obj):
        return f"TextNode({obj.text}, {obj.text_type}, {obj.url})"