import json
import threading
from pynput import mouse
import flet as ft
from pygetwindow import getWindowsWithTitle
from pywinauto import Application
 
# グローバル変数
events = []  # イベントデータを格納するリスト
 
def on_click(x, y, button, pressed):
    """マウスクリックイベントのリスナー関数"""
    if pressed:
        window_info = get_window_info(x, y)
        event = {
            'x': x,
            'y': y,
            'button': str(button),
            'window': window_info
        }
        events.append(event)
        print(event)  # デバッグ用
 
def get_window_info(x, y):
    """マウスポインタの位置にあるウィンドウの情報を取得"""
    for window in getWindowsWithTitle(""):
        if window.left < x < window.right and window.top < y < window.bottom:
            return {'title': window.title, 'position': (window.left, window.top)}
    return {}
 
def save_events():
    """イベントデータをJSONファイルに保存。見やすい形式で整形される。"""
    with open('events.json', 'w') as file:
        json.dump(events, file, indent=4)
 
def main_ui(page):
    # ElevatedButtonを使用してボタンを作成
    save_button = ft.ElevatedButton(text="Save Events", on_click=lambda e: save_events())
    page.add(save_button)
 
if __name__ == "__main__":
    # マウスリスナースレッドの開始
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()
 
    # Fletアプリケーションの実行
    ft.app(target=main_ui)
