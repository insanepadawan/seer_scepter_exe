import pyautogui
import time
import threading
import win32api, win32con
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods = ['GET'])


def get_articles():
    return jsonify({"hello": "world"})


def server_init():
    PORT = 8000
    server = HTTPServer(('', PORT), helloHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def accept_queue():
    print('checking')
    threading.Timer(5.0, accept_queue).start()
    location = pyautogui.locateAllOnScreen('accept2.png')

    for el in location:
        if el is not None:
            center_x = int(el.left + el.width / 2)
            center_y = int(el.top + el.height / 2)
            print(center_x, center_y)
            click(center_x, center_y)


def main():
    # acceptQueue()
    # server_init()
    if __name__ == '__main__':
        app.run(debug=True)

main()
