from simple_menu.items import FunctionItem
from simple_menu.items import MenuItem
from simple_menu.menu import Menu


def main():
    m = Menu()
    m.items.append(FunctionItem(label="test", function=lambda: print("test")))

    m2 = Menu(parent=m)
    m2.items.append(FunctionItem(label="test2", function=lambda: print("test2")))
    m.items.append(MenuItem(label="sub menu", menu=m2))

    m.run()


if __name__ == "__main__":
    main()
