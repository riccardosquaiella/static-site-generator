from __future__ import annotations

from enum import Enum

from leafnode import LeafNode


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:

    def __init__(self, text: str, text_type: TextType, url: str | None = None) -> None:

        if url is not None and text_type not in [TextType.LINK, TextType.IMAGE]:
            raise Exception("Only links and images can have an url")

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, value: object, /) -> bool:
        return (
            isinstance(value, TextNode)
            and value.text == self.text
            and value.text_type == self.text_type
            and value.url == self.url
        )

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            props = {"href": "" if text_node.url is None else text_node.url}
            return LeafNode("a", text_node.text, props)
        case TextType.IMAGE:
            props = {
                "src": "" if text_node.url is None else text_node.url,
                "alt": text_node.text,
            }
            return LeafNode("img", "", props)
        case _:
            raise ValueError("unknown text_type")
