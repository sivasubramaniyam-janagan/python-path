"""
Weather app — PyQt5 with a glass-style UI.
Uses Open-Meteo (no API key): geocoding + current weather.
"""

import sys
from typing import Optional, Tuple

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QColor, QFont, QLinearGradient, QPainter
from PyQt5.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


def temp_emoji(celsius: float) -> str:
    if celsius <= -10:
        return "🥶"
    if celsius <= 0:
        return "❄️"
    if celsius <= 10:
        return "🧥"
    if celsius <= 18:
        return "🌤️"
    if celsius <= 25:
        return "😊"
    if celsius <= 32:
        return "🌡️"
    if celsius <= 38:
        return "🥵"
    return "🔥"


def fetch_coords(city: str) -> Optional[Tuple[float, float, str]]:
    city = city.strip()
    if not city:
        return None
    r = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={"name": city, "count": 1, "language": "en", "format": "json"},
        timeout=12,
    )
    r.raise_for_status()
    data = r.json()
    results = data.get("results") or []
    if not results:
        return None
    loc = results[0]
    lat = float(loc["latitude"])
    lon = float(loc["longitude"])
    name = loc.get("name", city)
    admin = loc.get("admin1")
    country = loc.get("country", "")
    label = name
    if admin:
        label = f"{name}, {admin}"
    if country:
        label = f"{label}, {country}"
    return lat, lon, label


def fetch_weather(lat: float, lon: float) -> Tuple[float, int]:
    r = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m",
            "temperature_unit": "celsius",
        },
        timeout=12,
    )
    r.raise_for_status()
    cur = r.json().get("current") or {}
    temp = float(cur.get("temperature_2m", 0))
    humidity = int(cur.get("relative_humidity_2m", 0))
    return temp, humidity


class GradientBackground(QWidget):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        g = QLinearGradient(0, 0, self.width(), self.height())
        g.setColorAt(0.0, QColor(30, 60, 120))
        g.setColorAt(0.45, QColor(80, 40, 120))
        g.setColorAt(1.0, QColor(20, 90, 140))
        painter.fillRect(self.rect(), QBrush(g))


class GlassCard(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("glassCard")
        self.setStyleSheet(
            """
            QFrame#glassCard {
                background-color: rgba(255, 255, 255, 38);
                border: 1px solid rgba(255, 255, 255, 120);
                border-radius: 18px;
            }
            """
        )


class WeatherWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather")
        self.setMinimumSize(420, 480)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)

        root = QVBoxLayout(self)
        root.setContentsMargins(16, 16, 16, 16)
        root.setSpacing(0)

        self.bg = GradientBackground()
        root.addWidget(self.bg, stretch=1)

        inner = QVBoxLayout()
        inner.setContentsMargins(28, 28, 28, 28)
        inner.setSpacing(18)
        self.bg.setLayout(inner)

        title = QLabel("Weather")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(
            "color: rgba(255,255,255,230); font-size: 26px; font-weight: 600; "
            "letter-spacing: 1px; background: transparent;"
        )
        inner.addWidget(title)

        search_row = QHBoxLayout()
        search_row.setSpacing(10)
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search city…")
        self.search.setClearButtonEnabled(True)
        self.search.returnPressed.connect(self.on_search)
        self.search.setStyleSheet(
            """
            QLineEdit {
                background-color: rgba(255, 255, 255, 55);
                border: 1px solid rgba(255, 255, 255, 100);
                border-radius: 14px;
                padding: 12px 16px;
                color: #1a1a2e;
                font-size: 15px;
                selection-background-color: rgba(80, 120, 200, 180);
            }
            QLineEdit:focus {
                border: 1px solid rgba(255, 255, 255, 180);
                background-color: rgba(255, 255, 255, 75);
            }
            """
        )
        self.btn = QPushButton("Search")
        self.btn.setCursor(Qt.PointingHandCursor)
        self.btn.clicked.connect(self.on_search)
        self.btn.setStyleSheet(
            """
            QPushButton {
                background-color: rgba(255, 255, 255, 85);
                color: #1a1a2e;
                border: 1px solid rgba(255, 255, 255, 140);
                border-radius: 14px;
                padding: 12px 22px;
                font-size: 15px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 115);
            }
            QPushButton:pressed {
                background-color: rgba(255, 255, 255, 65);
            }
            """
        )
        search_row.addWidget(self.search, stretch=1)
        search_row.addWidget(self.btn)
        inner.addLayout(search_row)

        self.card = GlassCard()
        card_l = QVBoxLayout(self.card)
        card_l.setContentsMargins(24, 28, 24, 28)
        card_l.setSpacing(14)

        self.place_label = QLabel("Enter a city and tap Search")
        self.place_label.setAlignment(Qt.AlignCenter)
        self.place_label.setWordWrap(True)
        self.place_label.setStyleSheet(
            "color: rgba(255,255,255,220); font-size: 14px; background: transparent;"
        )
        card_l.addWidget(self.place_label)

        self.emoji_label = QLabel("🌍")
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setStyleSheet(
            "font-size: 72px; background: transparent; padding: 8px;"
        )
        card_l.addWidget(self.emoji_label)

        self.temp_label = QLabel("— °C")
        self.temp_label.setAlignment(Qt.AlignCenter)
        f = QFont()
        f.setPointSize(42)
        f.setBold(True)
        self.temp_label.setFont(f)
        self.temp_label.setStyleSheet("color: rgba(255,255,255,245); background: transparent;")
        card_l.addWidget(self.temp_label)

        self.humidity_label = QLabel("Humidity: —")
        self.humidity_label.setAlignment(Qt.AlignCenter)
        self.humidity_label.setStyleSheet(
            "color: rgba(255,255,255,200); font-size: 18px; background: transparent;"
        )
        card_l.addWidget(self.humidity_label)

        foot = QLabel(
            '<a href="https://open-meteo.com" style="color: rgba(255,255,255,160);">Data: Open-Meteo</a>'
        )
        foot.setOpenExternalLinks(True)
        foot.setAlignment(Qt.AlignCenter)
        foot.setStyleSheet("font-size: 11px; background: transparent;")
        card_l.addWidget(foot)

        inner.addWidget(self.card, stretch=1)

        close_row = QHBoxLayout()
        close_row.addStretch()
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(36, 36)
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.clicked.connect(self.close)
        close_btn.setStyleSheet(
            """
            QPushButton {
                background-color: rgba(255, 255, 255, 40);
                color: rgba(255,255,255,220);
                border: 1px solid rgba(255,255,255,90);
                border-radius: 18px;
                font-size: 14px;
            }
            QPushButton:hover { background-color: rgba(255,80,80,120); }
            """
        )
        close_row.addWidget(close_btn)
        inner.insertLayout(0, close_row)

        self._drag_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._drag_pos and event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self._drag_pos)
            event.accept()
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self._drag_pos = None
        super().mouseReleaseEvent(event)

    def on_search(self):
        q = self.search.text().strip()
        if not q:
            QMessageBox.warning(self, "Weather", "Please enter a city name.")
            return
        self.btn.setEnabled(False)
        self.btn.setText("…")
        QApplication.processEvents()
        try:
            coords = fetch_coords(q)
            if not coords:
                QMessageBox.information(self, "Weather", f"No results for “{q}”.")
                return
            lat, lon, label = coords
            temp, humidity = fetch_weather(lat, lon)
            self.place_label.setText(label)
            self.emoji_label.setText(temp_emoji(temp))
            self.temp_label.setText(f"{temp:.1f} °C")
            self.humidity_label.setText(f"Humidity: {humidity}%")
        except requests.RequestException as e:
            QMessageBox.critical(
                self,
                "Weather",
                f"Could not reach the weather service.\n\n{e!s}",
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                "Weather",
                f"Something went wrong.\n\n{e!s}",
            )
        finally:
            self.btn.setEnabled(True)
            self.btn.setText("Search")


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 10))
    w = WeatherWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
