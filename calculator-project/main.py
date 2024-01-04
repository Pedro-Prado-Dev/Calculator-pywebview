import webview
from app import server

if __name__ == '__main__':
    webview.create_window('Flask example', server)
    webview.start()
