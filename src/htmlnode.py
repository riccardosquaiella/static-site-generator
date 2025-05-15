from __future__ import annotations


class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list[HTMLNode] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        if tag is not None and tag == "":
            raise ValueError("tag cannot be an empty string")
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        return (
            ""
            if self.props is None
            else "".join(map(lambda x: f' {x[0]}="{x[1]}"', self.props.items()))
        )

    def __repr__(self) -> str:
        children: str | None = (
            f"[{self.children if self.children is None else ', '.join(map(lambda x: str(x), self.children))}]"
        )
        return f"HTMLNode({self.tag}, {self.value}, {children}, {self.props})"
