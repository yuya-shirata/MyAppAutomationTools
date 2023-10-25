"""
WindowInfoExtractor.py

このプログラムは、現在動作しているすべてのウィンドウの情報を取得し、
その情報をコンソールに出力するとともに、テキストファイルに保存します。
取得する情報には、ウィンドウのタイトル、クラス名、位置とサイズが含まれます。
"""

from pywinauto import Desktop

desktop = Desktop(backend="uia")
windows = desktop.windows()

# ファイルを書き込みモードで開く
with open("WindowInfoReport.txt", "w", encoding="utf-8") as file:
    for win in windows:
        # ウィンドウの情報を変数に格納
        title_info = "Title: " + win.window_text()
        class_info = "Class: " + win.class_name()
        rectangle_info = "Rectangle: " + str(win.rectangle())
        separator = "------"

        # コンソールに出力
        print(title_info)
        print(class_info)
        print(rectangle_info)
        print(separator)

        # ファイルに出力
        file.write(title_info + "\n")
        file.write(class_info + "\n")
        file.write(rectangle_info + "\n")
        file.write(separator + "\n")
