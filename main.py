from simple_menu.items import FunctionItem
from simple_menu.items import MenuItem
from simple_menu.menu import Menu


def main():
    m = Menu(prompt="Main Menu")
    m.items.append(FunctionItem(label="Item 1", function=lambda: print("Item 2")))

    m2 = Menu(parent=m, prompt="Sub Menu 1")
    m2.items.append(FunctionItem(label="Item 2", function=lambda: print("Item 2")))
    m.items.append(MenuItem(label="Sub Menu 1", menu=m2))

    m.run()


if __name__ == "__main__":
    main()
