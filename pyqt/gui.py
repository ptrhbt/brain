import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class WebViewWindow(QMainWindow):
    def __init__(self, url):
        super().__init__()
        self.setWindowTitle("Dash inside PyQt app")
        self.setGeometry(0, 0, 3840, 2160)

        # Create the web view widget
        self.web_view = QWebEngineView()
        self.web_view.load(url)

        # Create the main layout and add the web view
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.web_view)

        # Set the main widget and layout
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WebViewWindow(QUrl("http://127.0.0.1:8050"))
    window.show()
    sys.exit(app.exec_())
