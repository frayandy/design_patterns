from abc import ABC, abstractmethod
from random import choice
from typing import Callable


class ButtonInterface(ABC):
    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def on_click(self, handler: Callable):
        pass


class WindowsButton(ButtonInterface):
    def render(self):
        print("Render Windows button")

    def on_click(self, handler: Callable):
        handler("Do some Windows stuff")


class HTMLButton(ButtonInterface):
    def render(self):
        print("Render HTML button")

    def on_click(self, handler: Callable):
        handler("Do some HTML stuff")


class Dialog(ABC):
    def render_button(self):
        button: ButtonInterface = self.create_button()
        button.on_click(lambda x: print(x))
        button.render()

    @abstractmethod
    def create_button(self) -> ButtonInterface:
        pass


class WindowsDialog(Dialog):
    def create_button(self) -> ButtonInterface:
        return WindowsButton()


class HTMLDialog(Dialog):
    def create_button(self) -> ButtonInterface:
        return HTMLButton()


if __name__ == '__main__':
    dialog_map = {"windows": WindowsDialog, "web": HTMLDialog}
    current_os = choice(list(dialog_map.keys()))
    dialog_class = dialog_map.get(current_os)
    dialog = dialog_class()
    dialog.render_button()
