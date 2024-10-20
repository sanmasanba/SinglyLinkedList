from typing import Any

#node
class Node:
    def __init__(self, val: Any, tail: Any = None) -> None:
        self.val = val
        self.tail = tail