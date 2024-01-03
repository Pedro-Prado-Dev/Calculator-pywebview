import webview
import time
from API import API

def load_html(window):
    with open('src/index.html', 'r') as file:
        html_content = file.read()
    with open('src/css/styles.css', 'r') as file:
        css_content = file.read()
    time.sleep(2)
    window.load_html(html_content)
    window.load_css(css_content)


def main():
    with open('src/components/home_screen.html', 'r') as file:
        html_content = file.read()
    api = API()
    window = webview.create_window(
        title="Teste pywebview",
        html=html_content,
        js_api=api,
        width=800,
        height=600
    )
    with open('src/css/styles.css', 'r') as file:
        css_content = file.read()
    webview.start(window.load_css(css_content), window)

if __name__ == '__main__':
    main()

