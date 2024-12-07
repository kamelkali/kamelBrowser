from urllib.parse import urlparse

import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *

from discordRP import *
from settings import setup_web_engine

os.environ["QTWEBENGINE_CHROMIUM_FLAGS"] = "--disable-gpu"


def is_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


class KamelBrowser:

    def __init__(self):

        discordRPC(self)
        print("Wczytano Discord")

        self.window = QWidget()
        self.window.setWindowIcon(QIcon('ico/ico.png'))

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QLineEdit()

        self.go_btn = QPushButton()
        self.go_btn.setIcon(QIcon("ico/go.png"))

        self.refresh_btn = QPushButton()
        self.refresh_btn.setIcon(QIcon("ico/refresh.png"))

        self.home_page = QPushButton()
        self.home_page.setIcon(QIcon("ico/home.png"))

        self.back_btn = QPushButton()
        self.back_btn.setIcon(QIcon("ico/back.png"))

        self.next_btn = QPushButton()
        self.next_btn.setIcon(QIcon("ico/next.png"))

        self.horizontal = QHBoxLayout()
        self.horizontal.addWidget(self.home_page)
        self.horizontal.addWidget(self.refresh_btn)
        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.next_btn)

        print("Wczytano przyciski")

        self.browser = QWebEngineView()
        print("Wczytano przeglądarkę")

        self.window.showMaximized()
        # setup_web_engine()

        self.url_bar.returnPressed.connect(lambda: self.navigate(self.url_bar.text()))
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.text()))
        self.refresh_btn.clicked.connect(self.browser.reload)
        self.back_btn.clicked.connect(self.browser.back)
        self.next_btn.clicked.connect(self.browser.forward)
        self.home_page.clicked.connect(lambda: self.browser.setUrl(QUrl("http://google.com")))
        print("Wczytano akcje przycisków")

        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)
        print("Wczytano layout")

        self.browser.setUrl(QUrl("http://google.com"))
        self.browser.setWindowTitle("Kamel Browser")

        self.browser.urlChanged.connect(self.url_change)
        self.browser.titleChanged.connect(self.title_update)

        self.window.setLayout(self.layout)
        self.window.show()
        print("Wczytano okno")

    def eventFilter(self, event):
        print(f"Key pressed: {event.key()}")
        if event.key() == Qt.Key_F5:
            print("F5 pressed, reloading browser")
            self.browser.reload()
        else:
            super().keyPressEvent(event)

    def navigate(self, url):
        query = self.url_bar.text().strip()
        if " " in query and "." in query:
            url = f'https://www.google.com/search?q={query}'
            self.browser.setUrl(QUrl(url))
        elif query.startswith('http://') or query.startswith('https://'):
            url = query
            self.browser.setUrl(QUrl(url))
        elif "." in query and not " " in query:
            url = "http://" + query
            self.browser.setUrl(QUrl(url))
        else:
            url = f'https://www.google.com/search?q={query}'
            self.browser.setUrl(QUrl(url))

    def url_change(self, q):
        title = self.browser.url().toDisplayString()
        self.url_bar.setText(str(title))

    def title_update(self):
        title = self.browser.page().title()
        if title:
            self.window.setWindowTitle(title + " - Kamel Browser")
            discord_site_change(self)
        else:
            self.window.setWindowTitle("Kamel Browser")
            discord_site_change(self)


app = QApplication([])
app.setApplicationName("Kamel Browser")
window = KamelBrowser()
app.exec()
