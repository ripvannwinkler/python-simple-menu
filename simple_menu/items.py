from typing import Callable
from typing import Dict
from typing import List


class BaseItem(object):
    def __init__(self, label: str = ""):
        self.label = label

    def exec(self):
        print(self.label)


class MenuItem(BaseItem):
    from .menu import Menu

    def __init__(self, label: str, menu: Menu):
        super().__init__(label)
        self.menu = menu

    def exec(self):
        self.menu.run()


class FunctionItem(BaseItem):
    def __init__(
        self,
        label,
        function: Callable,
        args: List | None = [],
        kwargs: Dict | None = {},
    ):
        super().__init__(label)
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def exec(self):
        self.function(*self.args, **self.kwargs)
