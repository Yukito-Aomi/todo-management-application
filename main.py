# -*- coding: UTF-8 -*-


import sys

from PyQt6.QtWidgets import QApplication

from todoapp import MainWindow


def main() -> None:
    """
    メイン関数
    """

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
