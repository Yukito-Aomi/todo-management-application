# -*- coding: UTF-8 -*-


from PyQt6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    """
    アプリケーションのメインとなるウィンドウ・クラス
    """

    # ウィンドウ・タイトルのデフォルト値
    DEFAULT_TITLE = 'To-Do Manager'

    # ウィンドウ・サイズのデフォルト値
    DEFAULT_WIDTH = 480
    DEFAULT_HEIGHT = 640
    DEFAULT_SIZE = (DEFAULT_WIDTH, DEFAULT_HEIGHT)

    def __init__(self, size: tuple[int, int] = DEFAULT_SIZE) -> None:
        """
        コンストラクタ
        :param size: ウィンドウ・サイズ（横幅／縦幅）
        """

        super().__init__()

        # ウィンドウ・タイトルの設定
        self.setWindowTitle(self.DEFAULT_TITLE)

        # ウィンドウ・サイズの設定
        self.width = size[0]
        self.height = size[1]
        self.setFixedSize(self.width, self.height)

    def __del__(self) -> None:
        """
        デストラクタ
        """
        pass
