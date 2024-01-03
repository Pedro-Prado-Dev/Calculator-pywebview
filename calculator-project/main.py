import webview
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='frontend')

@app.route('/')
def serve_vue_app():
    return send_from_directory('frontend', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('frontend', filename)

def create_window():
    webview.create_window('Calculadora', 'http://127.0.0.1:5000/')
    webview.start(debug=True)

if __name__ == '__main__':
    import threading

    flask_thread = threading.Thread(target=app.run, kwargs={'debug': False})
    flask_thread.daemon = True
    flask_thread.start()

    import time
    time.sleep(2)

    create_window()
