from pywinauto import Desktop
import sys
import io

if sys.stdout:
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def print_window_info(win, file, indent=0):
    """ウィンドウの情報を出力する関数"""
    title_info = "Title: " + win.window_text()
    class_info = "Class: " + win.class_name()
    control_type_info = "Control Type: " + win.element_info.control_type
    rectangle_info = "Rectangle: " + str(win.rectangle())
    pid_info = "PID: " + str(win.process_id())
    
    # インデントを追加
    indent_str = "    " * indent
    
    # コンソールに出力
    print(indent_str + title_info)
    print(indent_str + class_info)
    print(indent_str + control_type_info)
    print(indent_str + rectangle_info)
    print(indent_str + pid_info)
    
    # ファイルに出力
    file.write(indent_str + title_info + "\n")
    file.write(indent_str + class_info + "\n")
    file.write(indent_str + control_type_info + "\n")
    file.write(indent_str + rectangle_info + "\n")
    file.write(indent_str + pid_info + "\n")

    # 特定のコントロールの情報を取得
    if "Edit" in control_type_info:
        text_info = "Text: " + win.window_text()
        print(indent_str + text_info)
        file.write(indent_str + text_info + "\n")
    elif "List" in control_type_info:
        try:
            items = win.children()
            item_texts = [item.window_text() for item in items]
            items_info = "Items: " + ", ".join(item_texts)
            print(indent_str + items_info)
            file.write(indent_str + items_info + "\n")
        except Exception as e:
            error_info = "Error getting list items: " + str(e)
            print(indent_str + error_info)
            file.write(indent_str + error_info + "\n")
    elif "RadioButton" in control_type_info:
        try:
            is_selected = win.get_toggle_state() == 2
            selected_info = "Selected: " + str(is_selected)
            print(indent_str + selected_info)
            file.write(indent_str + selected_info + "\n")
        except Exception as e:
            error_info = "Error getting check state: " + str(e)
            print(indent_str + error_info)
            file.write(indent_str + error_info + "\n")

    separator = "------"
    print(indent_str + separator)
    file.write(indent_str + separator + "\n")

    # 子要素の情報も出力
    for child in win.children():
        print_window_info(child, file, indent + 1)

# このプログラムは、デスクトップ上のすべてのウィンドウとその子要素の情報を取得し、
# それをテキストファイルに出力します。特定のコントロールの情報も取得されます。
desktop = Desktop(backend="uia")

# ファイルを書き込みモードで開く
with open("DetailedWindowInfoOutput.txt", "w", encoding="utf-8") as file:
    for win in desktop.windows():
        print_window_info(win, file)
