from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: dict[str, str] | None = None,
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag")
        if self.children is None:
            raise ValueError("missing children")
        children = "".join(map(lambda x: x.to_html(), self.children))
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"
