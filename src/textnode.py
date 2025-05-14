from __future__ import annotations

from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
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
