from typing import List


class Menu:
    def __init__(
        self,
        prompt="Choose:",
        prompt_quit="Quit",
        prompt_go_back="Go Back",
        parent: "Menu|None" = None,
    ):
        from .items import BaseItem

        self.prompt = prompt
        self.prompt_quit = prompt_quit
        self.prompt_go_back = prompt_go_back
        self.items: List[BaseItem] = []
        self.parent = parent

    def run(self):

        while True:

            print()
            print(self.prompt)

            index = 0

            for index, item in enumerate(self.items, start=1):
                print(f"{index}: {item.label}")

            if self.parent:
                index += 1
                print(f"{index}: {self.prompt_go_back}")

            index += 1
            print(f"{index}: {self.prompt_quit}")

            try:
                choice = int(input("> ").strip()) - 1

                if 0 <= choice < len(self.items):
                    self.items[choice].exec()
                    continue

                elif self.parent and choice == len(self.items):
                    break

                exit(0)

            except Exception as e:
                print(f"Error: {e}")
                continue
